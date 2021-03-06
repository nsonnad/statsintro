.. image:: ..\Images\title_continuous.png
    :height: 100 px

.. Test of Means of Continuous Data

Distribution of a Sample Mean
-----------------------------

One sample t-test for a mean value
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If we knew the mean and the standard deviation of a normally distributed
population, we would know exactly the standard error, and use values
from the normal distribution to determine how likely it is to find a
certain mean value, given the population mean and standard deviation.
However, in practice we have to *estimate* the mean and standard
deviation from the sample, and the resulting distribution for the mean
value deviates slightly from a normal distribution. Such distributions
are called *t-distributions*, and were first described by a researcher
working under the pseudonym of "Student".

Let us look at a specific example: we take 100 normally distributed
data, with a mean of 7 and with a standard deviation of 3. What is the
chance of finding a mean value at a distance of 0.5 or more from the
mean:?

See also the ipython notebook `oneSample.ipynb <http://nbviewer.ipython.org/url/raw.github.com/thomas-haslwanter/statsintro/master/ipynb/oneSample.ipynb>`_:

.. literalinclude:: ..\Code3\oneSample.py

:math:`>>>` The probability from the t-test is 0.057, and from the
normal distribution 0.054

Wilcoxon signed rank sum test
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If our data are not normally distributed, we cannot use the t-test
(although this test is fairly robust against deviations from normality).
Instead, we must use a *non-parametric* test on the mean value. We can
do this by performing a *Wilcoxon signed rank sum test*.  

(The following description and example has been taken from Altman, Table
9.2)

This method has three steps:

#. Calculate the difference between each observation and the value of
   interest.

#. Ignoring the signs of the differences, rank them in order of
   magnitude.

#. Calculate the sum of the ranks of all the negative (or positive)
   ranks, corresponding to the observations below (or above) the chosen
   hypothetical value.

In Table [tab:wilcoxon] you see an example, where the significance to a
deviation from the value of 7725 is tested. The rank sum of the negative
values gives :math:`3+5=8`, and can be looked up in the corresponding
tables to be significant. In practice, your computer program will
nowadays do this for you. This example also shows another feature of
rank evaluations: tied values (here :math:`7515`) get accorded their
mean rank (here :math:`1.5`).

======= ======================== ======================= =====================
Subject Daily energy intake (kJ) Difference from 7725 kJ Ranks of differences
======= ======================== ======================= =====================
 1       5260                    2465                    11
 2       5470                    2255                    10
 3       5640                    2085                    9
 4       6180                    1545                    8
 5       6390                    1335                    7
 6       6515                    1210                    6
 7       6805                    920                     4
 8       7515                    210                     1.5
 9       7515                    210                     1.5
 10      8230                    -505                    3
 11      8770                    -1045                   5
======= ======================== ======================= =====================

Comparison of Two Groups
------------------------

When you compare two groups with each other, we have to distinguish
between two cases. In the first case, we compare two values recorded
from the same subject at two specific times. For example, we measure the
size of students when they enter primary school and after their first
year, and check if they have been growing. Since we are only interested
in the *difference* between the first and the second measurement, this
test is called *paired t-test*, and is essentially equivalent to a
one-sample t-test for the mean difference.

The second test is if we compare two independent groups. For example, we
can compare the effect of a two medications given to two different
groups of patients, and compare how the two groups respond. This is
called an *unpaired t-test*, or *t-test for two independent groups*.

If we have two independent samples the variance of the difference
between their means is the *sum* of the separate variances, so the
standard error of the difference in means is the square root of the sum
of the separate variances:

.. math::

   \begin{aligned}
      se({{\bar x}_1} - {{\bar x}_2}) &= \sqrt {\operatorname{var} ({{\bar x}_1}) + \operatorname{var} ({{\bar x}_2})}  \\
      &= \sqrt {{{\left\{ {se({{\bar x}_1})} \right\}}^2} + {{\left\{ {se({{\bar x}_2})} \right\}}^2}}  \\
      &= \sqrt {\frac{{s_1^2}}{{{n_1}}} + \frac{{s_2^2}}{{{n_2}}}}  \\\end{aligned}

where :math:`\bar{x}_i` is the mean of the i-th sample, and *se*
indicates the *standard error*.


Non-parametric Comparison of Two Groups: Mann-Whitney Test 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If the measurement values from the two groups are not normally
distributed we have to resort to a non-parametric test. The most common
test for that is the *Mann-Whitney(-Wilkoxon) test*.

See also the ipython notebook `twoSample.ipynb <http://nbviewer.ipython.org/url/raw.github.com/thomas-haslwanter/statsintro/master/ipynb/twoSample.ipynb>`_:

.. literalinclude:: ..\Code3\twoSample.py

Comparison of More Groups
-------------------------

.. _`one-way ANOVAs`:

Analysis of Variance 
~~~~~~~~~~~~~~~~~~~~~~

The idea behind the *ANalysis Of VAriance (ANOVA)* is to divide the variance into
the variance *between* groups, and that *within* groups, and see if those
distributions match the null hypothesis that all groups come from the same
distribution. The variables that distinguish the different groups are often
called *factors*. (By comparison, t-tests look at the mean values of two groups,
and check if those are consistent with the assumption that the two groups come
from the same distribution.)

For example, if we compare a group with No treatment, another with treatment A,
and a third with treatment B, then we perform a *one factor ANOVA*, sometimes also
called *one-way ANOVA*, with "treatment" the one analysis factor. If we do the same
test with men and with women, then we have a *two-factor* or *two-way ANOVA*, with
"gender" and "treatment" as the two treatment factors. Note that with ANOVAs, it
is quite important to have exactly the same number of samples in each analysis
group!

Because the null hypothesis is that there is no difference between the
groups, the test is based on a comparison of the observed variation between the
groups (i.e. between their means) with that expected from the observed
variability between subjects. The comparison takes the general form of an F test
to compare variances, but for two groups the t test leads to exactly the same
answer.

The one-way ANOVA assumes all the samples are drawn from normally
distributed populations with equal variance. To test this assumption, you can
use the *Levene test*.

ANOVA uses traditional standardized terminology. The definitional equation
of sample variance is :math:`s^2=\textstyle\frac{1}{n-1}\sum(y_i-\bar{y})^2`,
where
the divisor is called the degrees of freedom (DF), the summation is called
the sum of squares (SS), the result is called the mean square (MS) and the
squared terms are deviations from the sample mean. ANOVA estimates 3 sample
variances: a total variance based on all the observation deviations from the
grand mean, an error variance based on all the observation deviations from
their appropriate treatment means and a treatment variance. The treatment
variance is based on the deviations of treatment means from the grand mean,
the result being multiplied by the number of observations in each treatment
to account for the difference between the variance of observations and the
variance of means. If the null hypothesis is true, all three variance
estimates are equal (within sampling error).

The fundamental technique is a partitioning of the total sum of squares SS
into components related to the effects used in the model. For example, the
model for a simplified ANOVA with one type of treatment at different levels.

.. math:: SS_\text{Total} = SS_\text{Error} + SS_\text{Treatments}

The number of degrees of freedom DF can be partitioned in a similar way: one
of these components (that for error) specifies a chi-squared distribution
which describes the associated sum of squares, while the same is true for
"treatments" if there is no treatment effect.

.. math:: DF_\text{Total} = DF_\text{Error} + DF_\text{Treatments} 


Example: one-way ANOVA 
~~~~~~~~~~~~~~~~~~~~~~~~

As an example, let us take the red cell folate levels (:math:`\mu g/l`)
in three groups of cardiac bypass patients given different levels of
nitrous oxide ventilation (Amess et al, 1978), described in the Python code example
below. I first show the result of this ANOVA test, and then explain the steps
to get there.

:: 

                DF     SS       MS       F   p(>F)
  C(treatment)   2  15515.76  7757.88  3.71  0.043
  Residual      19  39716.09  2090.32   NaN    NaN


-  First the "Sums of squares (SS)" are calculated. Here the SS between
   treatments is 15515.88, and the SS of the residuals is 39716.09 . The
   total SS is the sum of these two values.

-  The mean squares ("MS") is the SS divided by the corresponding degrees of
   freedom ("df").

-  The *F-test* or *variance ratio test*  is used for comparing the factors
   of the total deviation. The F-value is the larger mean squares value
   divided by the smaller value. (If we only have two groups, the F-value is
   the square of the corresponding t-value. See listing below.)


.. math:: 

    F = \frac{\text{variance between treatments}}{\text{variance within treatments}}

    F = \frac{MS_\text{Treatments}}{MS_\text{Error}} = {{SS_\text{Treatments} / (I-1)} \over {SS_\text{Error} / (n_T-I)}} 


-  Under the null hypothesis that two normally distributed populations have
   equal variances we expect the ratio of the two sample variances to have an
   :ref:`F Distribution`. From the F-value, we can look up the corresponding p-value.


See also the ipython notebook `anovaOneway.ipynb <http://nbviewer.ipython.org/url/raw.github.com/thomas-haslwanter/statsintro/master/ipynb/anovaOneway.ipynb>`_:

.. literalinclude:: ..\Code3\anovaOneway.py


Multiple Comparisons
~~~~~~~~~~~~~~~~~~~~~

The Null hypothesis in a one-way ANOVA is that the means of all the samples are the same. So if a one-way ANOVA yields a significant result, we only know that they are
*not* the same.

However, often we are not just interested in the joint hypothesis if all samples are the same, but we would also like to know for which pairs of samples the hypothesis of equal values is rejected. In this case we conduct several tests at the same time, one test for each pair of samples. (Typically, this is done with *t-tests* )

This results, as a consequence, in a *multiple testing problem*:
since we perform multiple comparison tests, we should compensate for the risk of getting a significant result, even if our null hypothesis is true. This can be cone by correcting the p-values to account for this. We have a number of options to do so:

- Tukey HSD
- Bonferroni correction
- Holms correction
- ... and others ...

Tukey's Test
^^^^^^^^^^^^

*Tukey's test*, sometimes also referred to as the *Tukey Honest Significant Difference (HSD) method*, controls for the Type I error rate across multiple comparisons and is generally considered an acceptable technique. It is based on a formula very similar to that of the t-test. In fact, Tukey's test is essentially a t-test, except that it corrects for multiple comparisons.

The formula for Tukey's test is:

.. math::    q_s = \frac{Y_A - Y_B}{SE}

where :math:`Y_A` is the larger of the two means being compared, :math:`Y_B` is the smaller of the two means being compared, and :math:`SE` is the standard error of the data in question. This :math:`q_s` value can then be compared to a q value from the *studentized range distribution*, which takes into account the multiple comparisons. If the qs value is larger than the critical value obtained from the distribution, the two means are said to be significantly different.
Note that the studentized range statistic is the same as the t-statistic except for a scaling factor (np.sqrt(2)).

.. literalinclude:: ..\Code3\multipleTesting.py

.. image:: ..\Images\MultComp.png
    :height: 500 px

*Comparing the means of multiple groups - here three different treatment options.*

Bonferroni correction 
^^^^^^^^^^^^^^^^^^^^^^^

Tukey's studentized range test (HSD) is a test specific to the comparison of all pairs of k independent samples. Instead we can run t-tests on all pairs, calculate the p-values and apply one of the p-value corrections for multiple testing problems. The simplest - and at the same time quite conservative - approach is to divide the required p-value by the number of tests that we do (*Bonferroni correction*). For example, if you perform 4 comparisons, you check for significance not at *p=0.05*, but at *p=0.0125*.

While multiple testing is not yet included in Python standardly, you can
get a number of multiple-testing corrections done with the statsmodels
package:

::

      In[7]: from statsmodels.sandbox.stats.multicomp import multipletests
      In[8]: multipletests([.05, 0.3, 0.01], method='bonferroni')
      Out[8]:
      (array([False, False,  True], dtype=bool),
      array([ 0.15,  0.9 ,  0.03]),
      0.016952427508441503,
      0.016666666666666666)

Kruskal-Wallis test 
~~~~~~~~~~~~~~~~~~~~~

When we compare two groups to each other, we use the *t-test* when the
data are normally distributed and the non-parametric *Mann-Whitney
test* otherwise. For three or more groups, the test for normally distributed
data is the *ANOVA-test*; for not-normally distributed data, the
corresponding test is the *Kruskal-Wallis test*. When the null
hypothesis is true the test statistic for the Kruskal-Wallis test follows
the *Chi squared distribution*.

.. literalinclude:: ..\Code3\KruskalWallis.py


Exercises
---------

One or Two Groups
~~~~~~~~~~~~~~~~~

#. **Wilcoxon signed rank sum test**

    The daily energy intake from 11 healthy women is [5260., 5470., 5640., 6180., 6390., 6515., 6805., 7515., 7515., 8230., 8770.] kJ. The data are clearly not normally distributed.

    Is this value significantly different from the recommended value of 7725?
     (Correct answer: yes, p=0.018)

#. **t-test of independent samples**

    In a clinic, 15 lacy patients weight [76., 101., 66., 72., 88., 82., 79., 73., 76., 85., 75., 64., 76., 81., 86.] kg, and 15 sporty patients weigh [ 64., 65., 56., 62., 59., 76., 66., 82., 91., 57., 92., 80., 82., 67., 54.] kg.

    Are the lacy patients significantly heavier?
     (Correct answer: yes, p=0.045)

#. **Kolmogoriv-Smirnov test**

    Are the two datasets normally distributed?
     (Correct answer: yes, they are)

#. **Mann-Whitney test**

    Are the lacy patients still heavier, if you check with the Mann-Whitney test?
     (Correct answer: yes, p=0.039)

Multiple Groups
~~~~~~~~~~~~~~~

(The following example is taken from the really good, but somewhat advanced book by AJ Dobson: "An Introduction to Generalized Linear Models")

#. **Get the data**

    The file   *https://github.com/thomas-haslwanter/statsintro/blob/master/Data/data\_others/Table 6.6 Plant experiment.xls* contains data from an experiment with plants in three different growing conditions. Get the data into Python.
    Hint: use the module xlrd

#. **Perform an ANOVA**

    Are the three groups different?
     (Correct answer: yes, they are.)

#. **Multiple Comparisons**

    Using the Tukey test, which of the pairs are different?
     (Correct answer: only TreamtmentA and TreatmentB differ)

#. **Kruskal-Wallis**

    Would a non-parametric comparison lead to a different result?
     (Correct answer: no)


