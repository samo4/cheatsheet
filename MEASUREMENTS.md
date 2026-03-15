---
title: "Measurements notes"
author: "Samo F."
header-includes:
  - |
    \usepackage[leftline,framemethod=TikZ]{mdframed}
    \renewenvironment{quote}{\begin{mdframed}[linecolor=gray!80, linewidth=3pt, leftline=true, rightline=false, topline=false, bottomline=false, innertopmargin=6pt, innerbottommargin=6pt, innerleftmargin=12pt, backgroundcolor=gray!5]}{\end{mdframed}}
bibliography: pandoc.bib
# csl: https://www.zotero.org/styles/ieee
csl: https://www.zotero.org/styles/harvard-cite-them-right
link-citations: true
extensions:
  - +auto_identifiers
---

# Measurements - a night time story

<!---

- introduce the concept of trust (a special version of mechanistic and not psychological trust):
  - common context and norms (language)
  - reliablility in the past
- do you trust a stranger to show up on time? You must first agree on the time (common language), then you can trust them based on their past behavior (reliability)
- in measurements artially resolve the first requirement for trust by introducing GUM (the second part of common language would be the SI units)
- GUM says that the uncertainty of our measurements should be expressed as standard deviation
- introduce uniform distribution using dice analogy
- and state that math says that standard deviation of uniform distribution is half_width/sqrt(3)
- manfuacturer of the instrument gave as a specification of limit of error (LOE)
- we assume uniform distribution of error within the LOE bounds (and we can convert it to standard uncertainty using the same formula as before)
- now we have two sources of uncertainty: quantization and instrument error
- since they are independent (one can point up and one down, thereby reducing the overall unceratinty) we can combine them using geometric sum
- the final uncertainty defines the precision of our measurement
- there are more sources of uncertainty but we will ignore them for now. Actually the quantization uncertainty is probably already included in the instrument error uncertainty.
- the elephant in the room is that manufacturer said someting and we trusted them. We also trusted that the instrument on the table was not tampered with or damaged in transport.
- it should be obvious now that we have a measured value with a certain uncertainty, but we don't know the "true" value.
- GUM dislikes the term "true value" because in real‑world measurement, the true value is unknowable, unobservable, and perhaps not even well‑defined.
- this is a philosophical point, but the point is that uncertainty is not an error bar around the true value, but a reflection of our knowledge about the value.
- so "accuracy" is closeness to the true value (which we can't know), and "error" is difference between measured value and true value
- so we can never know the result accurately, but we can know how precise our knowledge is (the uncertainty)

-->

## Intro

## Just looking at it

[^1]. Where the value of resistor will fall within the range defined by the resolution is random, but the type of distribution is a usefull piece of information. In our case, all values in range are equally likely, so we have a uniform **distribution**.

## This subtle improvement in our knowledge comes at a cost: we had to trust that the ADC is well-behaved. And trust, as we shall see, is the currency of measurement.

What is **uncertainty** you say? It is the gap between what we measure and what we know. In our case, we know that the value is between 9.95 kΩ and 10.05 kΩ, but we don't know where exactly. The uncertainty is a way to express this gap in a standardized way. GUM says that the standard way to express uncertainty is to use standard deviation, and luckly for us, mathematicians tell us that we can convert the width of a uniform distribution into standard deviation using the formula:

$$u(G)_q = \frac{Q}{2\sqrt{3}}$$

To express what we know about our particular measurement so far, we need to communicate the value, the resolution, the distribution type (uniform) and the number of measurements like so:

$$R = 10.0\,k\Omega \quad , \quad u(R)_q = 0.029\,k\Omega \quad , \quad n=1$$

The gap between what we measure and what we know is called **uncertainty**. In this case, uncertainty stems from the limited resolution of the display. Other sources - temperature drift, electrical noise,... exist, but we cannot detect them by "just looking at it". At this stage, the resolution defines the boundary of our knowledge.

The result as written above, although technically correct and standard, leaves a lot of information out.

## The nightmare scenario aka "the outliers"

The instrument that you are using to measure the resistor was on the table when you arrived. You didn't see it being manufactured, you didn't see it being calibrated, you don't know if it was dropped or tampered with by a jester collegue. You just trust that it's working as expected.

Allow me to go on a tangent here and introduce another simple instrument: non-contact voltage tester. Looks like a pen with a single LED that lights up when you bring it close to a live wire (it also agressively beeps at you). The potential consequences of a false negative are, as you can imagine, quite dire. And a false negative can come just from a dead battery.

What you do depends on your risk tolerance (or what was drilled in trade school). Perhaps you know that the tester worked yesterday and you trust that it still works today. But a more prudent approach would be to test the tester on a known live wire before using it each day. What I'm describing here is a process of statistical control.

The same process can be applied to our DMM: you can test it on a known resistor before using it.

So, when do you proclaim that your DMM is working correctly (for the day)?

The DMM has a manufacturer specification for its MPE - Maximum Permissible Error. If the DMM reads a value that is within the MPE of the known resistor, you can proclaim that it's working correctly. If it doesn't, you have a problem. MPE is similar to the resolution of the display in the sense that it defines the boundary of our knowledge about the instrument's performance - manufacturer states that as long as the environmental conditions are withint the reference range, there is absolutely no way for the measurement to be outside of the MPE bounds. As to where the value will fall within the MPE bounds, we again assume a uniform distribution (which can be converted to standard uncertainty using the same formula as before).

Another problem that you might have noticed is that you need to trust the known resistor as well. In principle you can use any resistor to verify that nothing dramatic happened to your DMM from the last time you were using it. In practice you will most likely be using a special calibration resistor with a **calibration certificate**. The calibration certificate is a document issued by another party that states the value of the resistor and its uncertainty. And you might have guessed, you need to trust this other party (commonly an accredited calibration laboratory) as well.

Depending on the application, the consequences of a "bad" measurement can be more or less severe. Depending on your the application you must decide how much trust you need to put into the measurement. And trust in measurment is a collection of as many uncertainties as you can find.

Since you can't always know if an instrument is damaged, metrologists use Statistical Process Control (SPC). You measure a "known" object every morning. If the result jumps by 5%, you know the instrument is compromised before you start the day's work. Measuring the same part with two different instruments or two different operators. If they don't "overlap" within their stated uncertainties, you have a consistency error, signaling a hidden systematic problem.

In GUM language, this is part of Type B uncertainty evaluation:

You use your knowledge and experience to judge whether the instrument is behaving normally. If the check passes, you assume the calibration and uncertainty budget are still valid. If it fails, you stop and investigate.

But GUM usually doesn't care about such outliers - it assumes that the instrument is working as expected and that the uncertainty budget is valid. In other words, GUM assumes that the measurement is under statistical control. Uncertainty is only valid for a validated process. If the instrument is broken, the uncertainty statement is no longer a measurement; it is a fiction.

You don't "calculate" for a dropped tool; you discard the data. This is why "Quality Assurance" (the process) is as important as "Metrology" (the math).

### statistical control

Has this instrument demonstrated stable, predictable behavior over time?

The Philosophical Truth: Uncertainty is a statement of current knowledge. If your knowledge is wrong (because you didn't know the tool fell), your uncertainty statement is also wrong. The GUM isn't a magic wand; it's a "best-case" logic for an honest, well-maintained experiment

## PEBKAC

If you don't know that the leads have resistance, you've missed a systematic effect in your measurement model. In the eyes of the GUM, your measurement is "wrong" not because of a math error, but because your state-of-knowledge was incomplete.

Here is how the GUM reconciles that "unknown" uncertainty:

- The Responsibility of the Analyst: The GUM places the burden on the person making the measurement to identify all significant influence quantities. If you are unaware of lead resistance, your reported uncertainty will be underestimated because you haven't included that variance component.
- The "Incomplete Model" Problem: A measurement starts with a model (image.gif
  ). If you don't know leads have resistance, your model is simply image.gif
  . GUM-6 notes that an inadequate model is a major source of uncertainty.
- Discovery via Intercomparison: Often, these "unknown" systematic errors are only discovered when your results are compared to another laboratory or a Certified Reference Standard. If your result differs significantly from the reference beyond your stated uncertainty, it proves there is an uncorrected systematic effect you didn't account for.
- Transitioning to Type B: Once you do realize leads have resistance (even if you haven't measured them specifically), you can no longer ignore them. You would use a Type B evaluation—using "professional judgment" or "manufacturer specs"—to assign a probability distribution to that lead resistance and add it to your Uncertainty Budget.

The Philosophy of Doubt: The GUM defines uncertainty as "the doubt about the measurement result". If there are factors you are "ignorant" of, your uncertainty statement is technically invalid for traceability purposes until those factors are identified and quantified.

In short: If you don't know it exists, you can't reconcile it. The GUM’s "reconciliation" only begins once you acknowledge a possible source of error—at which point it stops being an "unknown error" and becomes a "quantifiable uncertainty"

## Uncertainties

### Type B

When you're collecting uncertainties you don't know when one is pointing up and when one is pointing down. So you can't just add them up, because that would be a very pessimistic approach. The standard way to combine independent uncertainties is to use the root-sum-square method (aka geometric sum):

$$u_c = \sqrt{u_1^2 + u_2^2 + ... + u_n^2}$$

Standard uncertainty is always the range within which the "true" value is expected to lie with a probability of approximately 68% (1 standard deviation) - using normal (Gaussian) distribution. We already saw a way to convert from a uniform distribution to standard uncertainty. One thing to note here is that you must be careful whether your data about uniform distribution covers the whole range or just half of the range. So when you have a full width of the distribution, you need to divide by 2 in the formula, as is the case when you have uncertainty arising from resolution:

$$u(G)_q = \frac{Q}{2\sqrt{3}}$$

When you have MPE, it's usually specified as +- a certain value, which means that the number given is already half of the full width of the distribution, so you don't need to divide again:

$$u(R)_n = \frac{M}{\sqrt{3}}$$

And then we have the third option, which is the calibration certificate. I stated earlier that it has a value of and its uncertainty, but I witheld that the specification of uncertainty in calibration certificate is not standard uncertainty, but expanded uncertainty. Expanded uncertainty is a multiple of standard uncertainty, where the multiple is called coverage factor (k). The coverage factor is usually 2, which means that the laboratory is more than 95% confident that the true value is within the stated range. To convert it to standard uncertainty, we need to divide by k:

$$u(C) = \frac{U}{k}$$

### Type A

And there's one more source of uncertainty that we haven't talked about yet. This is the uncertainty that arises from repeated measurements. If you take multiple measurements of the same quantity, you will get different values due to random fluctuations. You can easily calculate the standard deviation of these measurements and then convert to standard uncertainty.

$$u(A) = \frac{s}{\sqrt{n}}$$

Where s is the standard deviation of the measurements and n is the number of measurements. Statisticians call this the standard error of the mean.

## Improved measurement result

We're now ready to express our measurement result in a more complete way.

We find the datasheet to see a specification for MPE in the form of $M=±(1\% reading + 2 digits)$. The limit of error usually combines a relative part (1% of reading) and an absolute part (2 digits of the display). The absolute part usually accounts for the resolution of the display as well. We convert the relative limit of error into absolute limit of error for our measurement:

$$M = ±1\% \cdot 10.0\,k\Omega + 2 \cdot 0.1\,k\Omega = 0.3\,k\Omega$$

And then we calculate the standard uncertainty due to the instrument error (Type B evaluation) to express the improved measurement result:

$$R = 10.0\,k\Omega \quad , \quad u(R)_q = 0.029\,k\Omega \quad , \quad u(R)_n = 0.17\,k\Omega \quad, \quad n=1$$

And let's not forget to read this result as trully meaning not that the resistor is guaranteed to be within 10.0 kΩ ± 0.17 kΩ, but that we are 68% confident (1 standard deviation) that the true value is within these bounds.

## Reality check

Now you give the resistor to a colleague and he measures it with their own DMM. He got a different value, which is not suprising. They also got a different uncertainty, also not suprising. What is suprising to you is that the uncertainty intervals don't overlap. Who is right, who is wrong? If you bear with me, I'll try to show that both of you are right, but one of the measurements could be "beter" than the other.

First remember how we found a way to translate from manufacturer's limit of error (uniform distribution) to standard uncertainty (standard deviation). In a uniform distribution absolutely all values outside of the limits are impossible. You can't throw a seven with a dice. On the other hand, in a normal distribution values arbitrarily far away from the mean are improbable, but still possible. The Gaussian distribution function extends to infinity in both directions and never reaches zero.

So when you compare two measurements with standard uncertainties, no matter how different are the values and how big the uncertainty, you're always alowing for the situation where the "true" value is exactly the same. Just this is enough to reconcile any two measurements. However, the more different the values are, the less probable this situation is.

# The dreams of one true value

GUM...
lie vs trust

In the context of the ISO GUM (Guide to the Expression of Uncertainty in Measurement), the concept of a "true value" is treated as an unknowable ideal rather than a practical reality. The GUM shifts the focus from finding a single "true" number to establishing a range of values that can reasonably be attributed to the thing being measured (the measurand).

The GUM argues that since no measurement is perfect, the "true" value remains forever unknown. Even with the most advanced instruments, there is always some level of uncertainty that prevents us from reaching an absolute, exact value.

Instead of trying to calculate "error" (the difference between a measurement and an unknown truth), the GUM focuses on uncertainty, which is a parameter characterizing the dispersion of values you can justify based on your observations.

## Realist vs. Instrumentalist Perspectives

There is an ongoing philosophical debate within metrology regarding this:

- Realist View: Believes that a unique true value exists in nature independently, but we are just incapable of seeing it perfectly.
- Instrumentalist View: Argues that "true values" are just mental constructs or models used to describe results, and what matters is the consistency of the measurement procedure. Bayesian statistics can be seen as a way to formalize the instrumentalist perspective, where we update our beliefs about the value based on evidence and uncertainty.

In short, the GUM doesn't necessarily say a true value doesn't exist in a physical sense, but it asserts that it is operationally useless because we can never actually know it.

# Work in progress ------------------------------------------------ NOTES

Measurements are a way to communicate information about the real world and are dependent on the common language and common understanding. That's why most introductions to this topic start with SI units, but the agreement about how long a meters is is only a part of the story. Here we need to agree on how to express uncertainty as well. Some smart people have worked on this and there are international standards about it. The most widely used is ISO GUM. They decided that the standard way to express uncertainty is to use standard deviation (no pun intended).

While we often think of trust as a psychological concept, at its core it has a mechanical basis: **shared context** and **consistent behavior**.

Consider this analogy: if you and I need to coordinate meeting at 14:00, we first need to agree on what "14:00" means - do we use UTC? Local time? This is shared context or common language. Then, assuming we both show up on time as expected (based on past experience), we can coordinate reliably. These two mechanical elements - shared context and consistent behavior history - form the foundation of trust. Without shared context, communication fails. Without consistent behavior, predictions fail. Together, they enable prediction and coordination.

In measurements, we operationalize these two elements through standards. The SI units provide shared context for quantities. ISO GUM (Guide to the Expression of Uncertainty in Measurement) provides shared context for how to express uncertainty. Calibration and verification provide evidence of consistent behavior - that the instrument performs as expected and according to its specification.

Looking at the picture of our little measurement, you probably don't recognize the DMM brand. Is it a good DMM? Is it calibrated? Did it ever fall off the table? How old is it? All these questions are relevant, because they affect the uncertainty of the measurement.

Even if you buy your instrument from a reputable vendor, they don't expect you to trust them blindly. They provide a calibration certificate issued by an accredited calibration laboratory, where "accredited" means that the lab has been audited by another body and found competent to perform the calibration tasks they offer. It's all a chain of paper or a chain of trust.

The calibration certificate is valid only for a certain period of time. In that period you don't really know if the instrument is still good or not. You can only trust that it is. You can increase your subjective level trust by performing verification by yourself, e.g. by measuring the same resistor using another DMM (with its separate chain of trust).

Here we have two options: we can have a manfacturer stated specification about the performance of the instrument when it leaves the factory. Or we can have a detailed calibration certificate[^1], with actual calibration results - deviations from true values.

LEARN TO NOT TRUST AND POKE HOLES!

If you didn't develop the habit of questioning and critically evaluating information, now is the last time to cross this rubicon. You were conditioned to trust whatever "the authority" said, but now you need to learn to doubt everything, critically evaluate all the available information and poke holes in the information you receive. This is a skill that will serve you well in all aspects of life, not just in measurements. You need to learn to ask questions like: "How do I know this is true?", "What is the evidence?", "What are the assumptions?", "What are the limitations?", "What are the alternatives?".

# Error & accuracy

When we measure something, we are trying to find out the "true" value of the quantity. One might say (such as the grey beards at ISO) that word "true" is redundant, because there is only one value that the quantity has. Another way to say it is that the true value is the value we would get if we could measure with no uncertainty.

In our case, we are contemplating the true resistance of the resistor. However, we never know the true value. We can only estimate it by measuring. The difference between the measured value and the true value is called **error**. We calculate it simply as our value minus the true value:

$$E = x_{measured} - x_{true}$$

Since we don't know the true value, we can't calculate the error directly. However, the afformentioned chain of trust goes all the way to the very definition of the SI units, which as of 2019 are based on fundamental constants of nature - in other words, they have no uncertainty. Only each laboratory in the chain adds its own uncertainty to the measurement.

At our stage we assume that the true value is within the uncertainty bounds defined by our measurement. The smaller the uncertainty, the closer we are to the true value. The close we are to the true value, the more **accurate** our measurement is.

I'll spare you the target analogy, but do know that accuracy is closeness to the true value, in other words, absolute error.

Here's a philosophical point worth pondering: GUM deliberately avoids the term "true value" because in real-world measurement, the true value is unknowable, unobservable, and perhaps not even well-defined. The uncertainty is not an error bar around the true value - it is a reflection of our knowledge about the value. We can never know the result accurately (closeness to the unknowable true value), but we can know precisely how imprecise our knowledge is.

<!---
can trust->confidence

 - k factor
 - accuracy
- point:
  - doubt
-->

# Putting it all together

1. Assume the instrument is in statistical control  
   (because it has a valid calibration certificate, passes self-tests, or has known performance).

2. Assign uncertainties from calibration and specs  
   These already account for manufacturing imperfections, drift, and typical handling.

3. Perform repeatability tests (Type A)  
   This checks whether the instrument behaves normally today.

4. Combine uncertainties  
   Using the GUM law of propagation.

You don’t need to know whether the instrument was dropped — if it had been dropped, it would likely fail repeatability tests or be out of calibration.

# Things you can't live without

## Basics of math

Calculate undefined integral of $x^n$ (yes, I know, I know...):

$$\int x^n dx = \frac{x^{n+1}}{n+1} + C \quad , \quad n \neq -1$$

Take out the logarithm of a power:

$$\ln(x^n) = n \cdot \ln(x)$$

## Basics of electrotechnics

Calculate effective value of a periodic signal (RMS):

$$V_{rms} = \sqrt{\frac{1}{T}\int_0^T v(t)^2 dt}$$

Calculate average value of a periodic signal (AVG):

$$\bar{V} = \frac{1}{T}\int_0^T v(t) dt$$

Calculate combined resistance of two resistors in parallel:

$$R_{{\mathbin{\|}}} = \frac{R_1 R_2}{R_1 + R_2}$$

Shanon's amount of information:

$$S = \log_2(N)$$

First order response time constant:

$$ percentage = 1 - e^{-\frac{t}{\tau}} $$

Log scale conversion (voltage):

$$L_{dB} = 20 \cdot \log_{10}\left(\frac{V}{V_{ref}}\right)$$

Series connection of 1st order systems:

$$t_{rs}^2 =  t_1^2 + t_2^2 + ... $$

$$1/{f^2} = 1/{f_1^2} + 1/{f_2^2} + ... $$

## List of basic SI units

| Quantity            | Unit name | Unit symbol |
| ------------------- | --------- | ----------- |
| Length              | meter     | m           |
| Mass                | kilogram  | kg          |
| Time                | second    | s           |
| Electric current    | ampere    | A           |
| Temperature         | kelvin    | K           |
| Amount of substance | mole      | mol         |
| Luminous intensity  | candela   | cd          |

---

However, you can think of many situations where you need to really know the value. Here I am deliberately avoiding the two big measurement words: accuracy and precision. We will return to them soon. For now, consider examples where precise knowledge matters: a pilot verifying fuel quantity before takeoff, or a pharmaceutical company measuring drug concentrations. In such cases, the measurement must be trustworthy enough to guarantee safety.

# Footnotes

[^1]: There are a few more conditions for the normal distribution to arise
