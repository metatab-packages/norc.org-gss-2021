# General Social Survey 2021

## Caveats

This package is an extract meant for a specific workflow. For general analysis, you should almost certainly use an extract generated from the [GSS website](https://gss.norc.org/). 

## Using the Data Files


The variables in this package are almost entirely categorical, but the data is stored with codes, with the categorical labels stored seperately in the ``_labels`` reference. When opening the file with Metapack, the ``convert_categorical`` argument ( which defaults to ``True`` ) controls converting the codes to labels. 

    pkg.resource('gss_2021').dataframe(convert_categorical=True)

Because the default is ``True`` this should happen automatically when using ``.dataframe``, but it is good to know what is happening behind the scenes. 