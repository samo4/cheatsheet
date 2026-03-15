---
title: "Measurements - a night time story"
author: "Samo F."
header-includes:
  - |
    \usepackage{pgfplots}
    \usepackage[leftline,framemethod=TikZ]{mdframed}
    \renewenvironment{quote}{\begin{mdframed}[linecolor=gray!80, linewidth=3pt, leftline=true, rightline=false, topline=false, bottomline=false, innertopmargin=6pt, innerbottommargin=6pt, innerleftmargin=12pt, backgroundcolor=gray!5]}{\end{mdframed}}
bibliography: pandoc.bib
csl: https://www.zotero.org/styles/harvard-cite-them-right
link-citations: true
extensions:
  - +auto_identifiers
---

# When is a measurement more than just a number?

Picture this: it is late evening, you are in the lab, the coffee is cold, and the only thing still blinking with enthusiasm is a digital multimeter on the bench. You set it to $\Omega$ mode, clip two wires across a resistor, it says 10.0 kOhm, and for a moment the matter appears settled. In a lot of practical work that really is the end of the story. Many (if not most) circuits are so forgiving that even a wildly wrong resistor will not stop them from doing their job.

But not all measurements live in such a friendly territory. If that same resistor is being used as a temperature sensor, then a even a relatively reasonable error in resistance (say 5%) may be the difference between wearing shorts and freezing. In that setting, reading a number is not enough. The real question is what that blinking display is telling you - and what it isn't.

That is the thread running through this article: a displayed number is not the same thing as justified knowledge.

# One reading, one DMM

To keep the problem honest, start with the smallest possible measurement model. There is one measurand, the resistance of the resistor. There is one instrument, the DMM. There is one reading, so $n=1$. No repeated trials, no fancy statistics, no uncertainty budget spreadsheet yet. Just you, the resistor, and whatever the display is willing to confess.

We will start with a very simple observation: the display of the DMM can only show a certain number of digits. In our case, it shows as three digits, for a total value of 10.0 kΩ. The resolution of this display is 0.1 kΩ - it can't show us any more detail than that:

$$Q = 0.1\,k\Omega$$

If you only stare at the display and refuse to assume anything about what happens inside the meter, then 10.0 kOhm seems to mean that the actual value could be somewhere in a small neighborhood around that indication - if you're really pessimistic then the range is from 9.9 kΩ to 10.1 kΩ - a range of full 0.2 kΩ. If the DMM contains a well behaved ADC, then the meter does not merely chop values off; it rounds them. So a displayed value of 10.0 kOhm corresponds more naturally to:

$$9.95\,k\Omega \le R < 10.05\,k\Omega$$

Already there is something interesting hiding here. The move from the crude interval to the rounded interval is not something you observed directly. You accepted it because you trust the instrument to behave like a competent measuring device. Even in this toy example, _trust_ has entered the room.

Beyond this small concession we made to trust, we are still in the dark about where exactly the value is within that interval. Resistors are not magically obliged to be exactly 10.0 kOhm and we're not even asking the resistor, we're asking our instrument. Within that interval, the "real" value could be anywhere and all values are equally likely - similar to throwing a dice. We call this uniform (or rectangular) distribution.

# Language of uncertainty

If you do shout "it's ten" across the room, your colleague will only understand you if enough context is already shared. If you were both just discussing resistors, they will probably hear "10 kOhm." If not, you may get something less useful in return, like "ten oranges?". Measurement is communication, and communication works only if there's a shared language.

This is why metrology needs conventions.

If you're reading this, you probably already know what a meter is and you likely remember that it was conceived as an arbitrarily defined fraction of the Earth's meridian. It replaced a previous system where almost every village had its own definition of length. Today meter is a member of the _SI family of units_ on which basically the entire world agrees - giving us a shared language for quantities.

And then there is _the unknown_ as intuited when looking at the display. We can say "the resistor is somewhere between 9.95 and 10.05 kOhm," but that is not a very good way to talk about what we know. To prevent shouting and confusion, the metrology community has invented the [ISO GUM](https://www.bipm.org/documents/20126/2071204/JCGM_100_2008_E.pdf) (Guide to the Expression of Uncertainty in Measurement) to give us a shared language for uncertainty. The GUM is not a law of nature; it is a convention.

The point of SI units and GUM is to make measurements transportable. A result should mean roughly the same thing to the person who made it, the person who reads it tomorrow, and the laboratory on the other side of the planet.

In GUM language, uncertainty is expressed as a standard uncertainty, that is, in standard deviation form. Standard deviation simply states that 68% of the probability "mass" is contained within plus or minus one standard deviation of the mean.

```{=latex}
\begin{center}
\begin{tikzpicture}
\begin{axis}[
  width=10cm, height=5.5cm,
  axis x line=bottom,
  axis y line=none,
  xtick={-1, 0, 1},
  xticklabels={$\mu - u$, $\mu$, $\mu + u$},
  ymin=0, ymax=0.48,
  xmin=-3.5, xmax=3.5,
  domain=-3.5:3.5,
  samples=200,
  clip=false,
]
  \addplot[thick] {exp(-x^2/2)/sqrt(2*pi)};
  \addplot[fill=gray!30, fill opacity=0.6, draw=none, domain=-1:1]
    {exp(-x^2/2)/sqrt(2*pi)} \closedcycle;
  \node at (axis cs:0, 0.17) {$\approx 68\%$};
\end{axis}
\end{tikzpicture}
\end{center}
```

This is exactly where our humble DMM example fits in. We already know that the display gives us a bounded interval, and we already decided to model the values inside that interval with a uniform distribution basicly stating that we're certain that 100% of the values are within the interval.

If we wanted to translate that into GUM language, we would need to find the standard uncertainty corresponding to a uniform distribution with a full width of 0.1 kOhm.

Initial intuition might suggest that the standard uncertainty is simply the one that covers 68% of the area. But grey beards have decided for us that we want to preserve the variance of the distribution (minimum possible average penalty for being wrong). For a uniform distribution with full width $Q$, the corresponding standard uncertainty is:

$$u_q = \frac{Q}{2\sqrt{3}} = \frac{0.1\,k\Omega}{2\sqrt{3}} = 0.029\,k\Omega$$

So the first serious thing we can say about our toy resistance measurement is not merely that the resistor is 10.0 kOhm, but that our present state of knowledge can be written as:

$$R = 10.0\,k\Omega, \quad u_q = 0.029\,k\Omega, \quad n = 1$$

That statement is still incomplete, but it is already much better than simply shouting "it's ten" across the lab. At this stage, what we know comes only from the finite resolution of the display, so quantization is the only legitimate uncertainty contribution we have earned so far.

# Trust and instrument validity

The moment you stop looking only at the display, the whole quiet measurement becomes much less innocent. The DMM was already on the bench when you arrived. You did not witness its manufacture. You did not watch its calibration. You do not know whether somebody dropped it yesterday, borrowed it last week, or left it overnight in some hostile environment. In everyday practice you simply trust that it is behaving normally.

This kind of trust is not psychological in the soft sense of the word. It has a mechanical structure. First there must be shared context: units, conventions, procedures, specifications, all the things that let two people mean the same thing when they talk about a result. Second there must be a history of consistent behavior: the instrument must continue to perform the way it has performed in the past, or at least in a way compatible with its stated specification.

That is why verification matters. Consider a non-contact voltage tester, the little pen that lights up and beeps near a live conductor. A false negative there is not an academic inconvenience. It can come from something as stupid as a dead battery, and the consequences can be severe. The prudent habit is to check the tester on a known live source before relying on it. The same logic applies to the DMM: check it against something known before entrusting the day's work to it.

This is the practical meaning of statistical control. The uncertainty statement only makes sense if the measurement process is behaving normally. If the instrument is broken then no amount of elegant mathematics rescues the result. Uncertainty is valid only for a process that is under control. If the process is not valid, the measurement result is fiction.

# Type B uncertainty components

Once the process is assumed to be under control, we can start collecting uncertainty contributions that do not come from repeated measurements. GUM calls these Type B evaluations. The label sometimes makes them sound second-rate or approximate, but in practice they are often where most of the useful engineering knowledge sits: datasheets, certificates, previous calibrations, specifications, judgment about bounds, and experience with the instrument.

## Manufacturer limit (MPE / LOE)

Suppose the datasheet gives the meter accuracy in the form:

$$M = \pm(1\%\;\text{of reading} + 2\;\text{digits})$$

At a reading of 10.0 kOhm with a display step of 0.1 kOhm, this becomes:

$$M = \pm\left(0.01 \cdot 10.0\,k\Omega + 2\cdot0.1\,k\Omega\right) = \pm0.3\,k\Omega$$

What the manufacturer has given you here is not a standard uncertainty but a bound, a maximum permissible error or limit of error. If you decide that values inside that bound are reasonably modeled as uniformly distributed, then you can translate that bound into standard uncertainty using basicly the same formula as for quantization (the difference being that the bound is a half-width, while quantization was a full width):

$$u_M = \frac{M}{\sqrt{3}} = \frac{0.3\,k\Omega}{\sqrt{3}} = 0.173\,k\Omega$$

Again, there is trust embedded in the step. You are trusting not only the mathematics of the conversion, but also that the manufacturer's bound is meaningful for the instrument in front of you under the environmental conditions you are actually using.

What conditions? Well, if you take your DMM out into the Artic and try to measure the resistor there, the accuracy may be much worse than the datasheet suggests. As a matter of fact, the manufacturer states ranges of environmental conditions: reference and operating.

Environmental conditions can be anything that manufacturers think might affect the performance of the instrument: temperature, humidity, pressure to name a few. It's your job to be on the watch for others. For example a strong magnetic field can break havoc with any instrument.

Anyhow: if you're operating the instrument with its refernce condtions the MPE holds. If you're operating it with its operating conditions, the MPE may be worse. If you're operating it outside of the operating conditions, you already know what'll say: fiction.

## Calibration certificate values

Sometimes you have something better than a generic manufacturer specification: a calibration certificate. Some other party measured the instrument or a reference artifact, reported a value, and attached an uncertainty to it. In this particular case, the uncertainty is not reported as standard uncertainty but as expanded uncertainty $U$ with a coverage factor $k$, often $k=2$.

```{=latex}
\begin{center}
\begin{tikzpicture}
\begin{axis}[
  width=10cm, height=5.5cm,
  axis x line=bottom,
  axis y line=none,
  xtick={-2, 0, 2},
  xticklabels={$\mu - 2u$, $\mu$, $\mu + 2u$},
  ymin=0, ymax=0.48,
  xmin=-3.5, xmax=3.5,
  domain=-3.5:3.5,
  samples=200,
  clip=false,
]
  \addplot[thick] {exp(-x^2/2)/sqrt(2*pi)};
  \addplot[fill=gray!45, fill opacity=0.55, draw=none, domain=-2:2]
    {exp(-x^2/2)/sqrt(2*pi)} \closedcycle;
  \node at (axis cs:0, 0.15) {$\approx 95\%$};
\end{axis}
\end{tikzpicture}
\end{center}
```

To bring it into the same language as the rest of the budget, convert it using:

$$u_{cal} = \frac{U}{k}$$

This is a cleaner and more traceable form of knowledge than mere optimism, but it is still knowledge by delegation. You trust the laboratory, its methods, its accreditation, and the continuity of the chain from their equipment to yours.

## Model completeness note

There is also an uglier side to all this. If a significant effect is missing from your measurement model, then the uncertainty you report is understated no matter how carefully you computed it. If you are measuring low resistance and forget that leads have resistance too, the problem is not that your arithmetic failed. The problem is that your state of knowledge was incomplete. GUM cannot reconcile an effect that you never admitted existed. Once you identify it, it becomes a candidate for Type B treatment. Before that, it remains a hole in the model.

# One more time (Type A)

As your resistor (measurand) and your DMM (instrument) are sitting on the table as we're discussing them, you may be tempted to take another glance at the display. It shows a different value, only off by the least significant digit, but still different. What now?

The standard distribution is called "standard" because it's the most common. Mathematically it arises in all situations where many different effects combine to produce a result. The most widely cited example would be how many different genetic and environmental factors combine to produce a human height. Statisticians call this the central limit theorem.

When measuring our humble resistor, we too have many different effects combining to produce the displayed value: the actual resistance, the noise in the measurement, the temperature fluctuations. If we were to take many readings of the same resistor under the same conditions, we would see a distribution of values that is often well approximated by a normal distribution.

And we can use this effect to our advantage. If we take many readings ($n$), we can calculate the sample standard deviation $s$ of those readings, and then use that to estimate the uncertainty of the mean. This is what GUM calls Type A evaluation.

$$u_A = \frac{s}{\sqrt{n}}$$

And statisticians call it is the standard error of the mean. It captures repeatability, noise, short-term fluctuation, and all the random nonsense that reveals itself only by happening more than once.

You might wonder... if made a single reading then we wouldn't have Type A uncertainty, but if we made two readings then we would? And now we have additional uncertainty to add to our budget? So by making more measurements we are actually making our uncertainty worse?

If you look at the formula, you will see that the more readings we make, the smaller the Type A uncertainty becomes. For a single reading, the Type A uncertainty is still there, it's just unknowable.

This is the core tenet of GUM: uncertainty is not a property of the world, but a property of our state of knowledge. If we have only one reading, we have no way to know how much that reading might fluctuate if we were to repeat it. As we take more readings, we start to illuminate that darkness and get a better estimate of the true variability.

And this is not limited to Type A uncertainty. You can easily miss a certain Type B uncertainty. But the ones you do capture are the state of your knowledge. The more you know, the better your uncertainty statement becomes.

# The abacus of uncertainties

Once several uncertainty components are on the table, the next temptation is to add them directly. That would be safe in the sense of being pessimistic, but independent uncertainty contributions do not all push in the same direction at the same time. The standard way to combine them is therefore the root-sum-square rule:

$$u_c = \sqrt{u_1^2 + u_2^2 + \cdots + u_n^2}$$

One caution matters here more than any formula: do not count the same effect twice. Many DMM specifications already fold display resolution into the stated accuracy term. If you also carry a separate quantization term without thinking, you can make the budget look more rigorous while actually making it worse.

# Comparing two different measurements

Suppose you hand the resistor to a colleague and they measure (different person, different instrument, different everything but the resistor). They obtain a different value and a different uncertainty. None of that is surprising. What bothers people is when the two uncertainty intervals do not seem to overlap. The immediate instinct is to ask who is right and who is wrong.

That question is usually too blunt to be useful. A disagreement between results can mean several things: one uncertainty statement may be underestimated, one of the models may be missing an influence quantity, one process may no longer be under control, or the apparent contradiction may simply be less dramatic than it looks because the underlying probability models are different from the crude mental picture people attach to plus-minus notation.

Uniform bounds and Gaussian uncertainties do not behave the same way. A uniform model says values outside the limit are impossible. A Gaussian model says distant values are merely improbable. So comparison between measurements is best treated as a diagnostic exercise. It tells you to inspect the models and assumptions, not to declare a metaphysical winner.

# Error, accuracy, precision, and true value

At some point every discussion of measurement runs into the old dream of the true value. Formally, error is often written as:

$$E = x_{measured} - x_{true}$$

That equation is perfectly respectable, but it hides the hardest part of the problem in the subscript. In practical metrology the true value is not available for inspection. If it were, you would not need measurement in the first place. You can talk about error formally, and in calibration chains you can get closer and closer to a reference of higher quality, but the fully exact value remains operationally out of reach. It's a platonic ideal, not a practical reality.

This is why GUM prefers to organize thought around uncertainty rather than around an imagined direct grasp of truth. Precision is about spread, repeatability, and the scale of uncertainty. **Accuracy** is closeness to the true value, which is conceptually meaningful but practically limited by the fact that the true value is not something you can lay on the bench next to the resistor and compare against directly.

So the mature objective of measurement is not to claim the exact value. It is to provide a good estimate together with a good account of how **uncertain** that estimate remains.
