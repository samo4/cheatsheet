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

# Intro

# Just looking at it

The measurement task we will consider is measuring the resistance of a resistor using a digital multimeter (DMM). It doesn't get simpler than that: take the DMM, set it to resistance measurement mode, connect the two wires and read the value on the display. As a matter of fact, for a lot of purposes this is all you need - many practical electrical circuits are not very sensitive to variations in resistance values - they will work just fine even if the resistance is off by 50%.

However, you can think of many situations where you need to really know the value. Here I am deliberately avoiding the two big measurement words: accuracy and precision. We will return to them soon. For now, consider examples where precise knowledge matters: a pilot verifying fuel quantity before takeoff, or a pharmaceutical company measuring drug concentrations. In such cases, the measurement must be trustworthy enough to guarantee safety.

Our measurement task is now more complex: we need a value and a "guarantee" that the value is within certain bounds. Our DMM reads a number 10.0 kΩ. The is DMM can only show us 9.9kΩ, 10.0kΩ and 10.1kΩ. We physically can't read any more detail that, so the reading is only known within ±½ of the least significant digit (LSD). This is the first element of our "guarantee". The concept can also be applied to analog displays, and it is called **resolution** of the display (represneted by Q as "quant").

The measurement can fall in the range from 9.95 kΩ to 10.05 kΩ - all values in between are possible and indistinguishable by our DMM. More importantly, all values in that range are equally possible. This is different from the most famous distribution, the normal distribution, where values near the mean are more probable than values further away. Here we have equal probability for all values in the range. This is called a uniform or rectangular distribution.

The gap between what we measure and what we know is called **uncertainty**. In this case, uncertainty stems from the limited resolution of the display. Other sources - temperature drift, electrical noise,... exist, but we cannot detect them by "just looking at it". At this stage, the resolution defines the boundary of our knowledge.

# Communicating results

In order to communicate the measurement we now need four pieces of information: the measured value (10.0 kΩ), the resolution (Q=0.1 kΩ), the distribution type (uniform) and the number of measurements (N=1). The key word here is "communication". Measurements are a way to communicate information about the real world and are dependent on the common language and common understanding. That's why most introductions to this topic start with SI units, but the agreement about how long a meters is is only a part of the story. Here we need to agree on how to express uncertainty as well. Some smart people have worked on this and there are international standards about it. The most widely used is ISO GUM. They decided that the standard way to express uncertainty is to use standard deviation (no pun intended).

You may recall that standard deviation is closely related to normal (Gaussian) distribution. And that in turn implies that we need to take multiple samples (measurements) before we can say anything about standard deviation. In our case we have single measurement. How to reconcile that? The ISO standards body figured that out too. They defined something called "Type B evaluation of uncertainty" which deals with any situation where you don't have repeated measurements to calculate standard deviation from.

In short, they decided to use "scientific judgement" to estimate the standard deviation for different types of distributions even if you have only a single measurement. In our case we have uniform distribution with range of 0.1 kΩ to convert it into **standard uncertainty** we use the formula:

$$u(G)_q = \frac{Q_g}{2\sqrt{3}}$$

In this formula the number 2 follows from the fact that Q is the full-width of the distribution (from one edge to the other). The factor of 1/√3 comes directly from calculating the standard deviation of a rectangular distribution.

So, at this early stage, our result of a measurement can be provisionally expressed as:

$$R = 10.0\,k\Omega \pm 0.029\,k\Omega \quad , \quad n=1$$

Or if we follow ISO/IEC 80000 notation:

$$R = 10.0\,k\Omega \quad , \quad u(R)_q = 0.029\,k\Omega \quad , \quad n=1$$

But, is it really that simple? Would you trust this result? Let's step back a little bit.

# Trust

Trust is uniquely human concept. You could say that human civilization is built on trust supported by a whole lot of data. Stated as famous russian proverb: "Trust, but verify".

Looking at the picture of our little measurment, you probably don't recognize the DMM brand. Is it a good DMM? Is it calibrated? Did it ever fell off the table? How old is it? All these questions are relevant, because they affect the uncertainty of the measurement.

Even if you buy your instrument from a reputable vendor, they don't expect you to trust them blindly. They provide a calibration certificate issued by an accredited calibration laboratory, where "accredited" means that the lab has been audited by another body and found competent to perform the calibration tasks they offer. It's all a chain of paper or a chain of trust.

The calibration certificate is valid only for a certain period of time. In that period you don't really know if the instrument is still good or not. You can only trust that it is. You can increase your subjective level trust by performing verification by yourself, e.g. by measuring the same resistor using another DMM (with its separate chain of trust).

Here we have two options: we can have a manfacturer stated specification about the performance of the instrument when it leaves the factory. Or we can have a detailed calibration certificate[^1], with actual calibration results - deviations from true values.

## Manufacturer specification with limit of error

Manufacturer specifications usually state the limit of error of the instrument in a form such as $M=±(1\% reading + 2 digits)$. This means that for any measurement, the true value is within the range defined by the reading plus/minus the limit of error. The limit of error usually combines a relative part (1% of reading) and an absolute part (2 digits of the display). The absolute part usually accounts for the resolution of the display as well.

The limit of error is usually valid only under certain reference conditions (temperature, humidity, altitude,...). We also assume that the distribution density of error is uniform within the limits. So we can again use the formula for standard uncertainty for uniform distribution. Say that our DMM has limit of error of $M=±(1\% reading + 2 digits)$ if in temperature range from 18°C to 28°C, relative humidity below 80% and altitude below 2000m (and that the measurments on our picture were done in these conditions). We convert the relative limit of error into absolute limit of error for our measurement:

$$M = ±1\% \cdot 10.0\,k\Omega + 2 \cdot 0.1\,k\Omega = 0.3\,k\Omega$$

And then we calculate the standard uncertainty due to the instrument error (Type B evaluation):

$$u(R)_n = \frac{M}{\sqrt{3}}$$

We can now improve on our stated measurement result:

$$R = 10.0\,k\Omega \quad , \quad u(R) = 0.17\,k\Omega \quad, \quad n=1$$

And let's not forget to read this result as trully meaning not that the resistor is guaranteed to be within 10.0 kΩ ± 0.17 kΩ, but that we are 68% confident (1 standard deviation) that the true value is within these bounds. This range brings us to the next chapter:

## Calibration certificate with expanded uncertainty

A calibration certificate usually contains a table with measured values at multiple points. Each point has an associated expanded uncertainty - the laboratory is more than 68% confident that the adjusted measurement is with the stated range. Usually 95% confidencent - 2 standard deviations (k=2).

We combine the two pieces of information from the calibration certificate: we adjust (offset) the measured value by the error that the calibration laboratory found in our instrument. Then we adjust the uncertainty back to 1 standard deviation by dividing the expanded uncertainty by k.

# Error & accuracy

When we measure something, we are trying to find out the "true" value of the quantity. One might say (such as the grey beards at ISO) that word "true" is redundant, because there is only one value that the quantity has. Another way to say it is that the true value is the value we would get if we could measure with no uncertainty.

In our case, we are contemplating the true resistance of the resistor. However, we never know the true value. We can only estimate it by measuring. The difference between the measured value and the true value is called **error**. We calculate it simply as our value minus the true value:

$$E = x_{measured} - x_{true}$$

Since we don't know the true value, we can't calculate the error directly. However, the afformentioned chain of trust goes all the way to the very definition of the SI units, which as of 2019 are based on fundamental constants of nature - in other words, they have no uncertainty. Only each laboratory in the chain adds its own uncertainty to the measurement.

At our stage we assume that the true value is within the uncertainty bounds defined by our measurement. The smaller the uncertainty, the closer we are to the true value. The close we are to the true value, the more **accurate** our measurement is.

I'll spare you the target analogy, but do know that accuracy is closeness to the true value, in other words, absolute error.

# Summing up uncertainties & precision

When we have multiple sources of uncertainty, we need to combine them into a single standard uncertainty. The uncertainties that we're summing up are a reflection of an underlying random distribution, so we can't just add them linearly. Doing that would overestimate the combined uncertainty, becuase the underlying randomness sometimes adds up and sometimes cancels out. The standard way to do this is to use the root-sum-square (RSS) method (or geometric sum). This only works if the uncertainties are **really** independent and random.

$$u_c = \sqrt{u_1^2 + u_2^2 + ... + u_n^2}$$

Finally the number that we come up defines the **precision** of our measurement. Precision is closeness of agreement between repeated measurements. In other words, it is the size of the uncertainty interval.

[^1]: Calibration laboratories have a whole list of services that they provide. One service would be to just check (pass/fail) if your DMM is within the manufacturer specified limits. Another service would be to provide a detailed calibration certificate with actual measured deviations at multiple points. And sometimes the instrument allows for adjustment and the calibration lab can adjust it to bring it closer to true values.
