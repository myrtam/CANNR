\name{cnrToJSON}
\alias{cnrToJSON}
\title{Convert R object to JSON to be Returned by a CANNR Service}
\usage{
cnrToJSON(outputObject, outputParseType = 'default')
}
\description{
Converts an R object to a JSON string to be output by a CANNR service.
The output is of the form '{"data": <output data>}', e.g.,
'{"data": [{"a": 1, "b": 2, "c": 3}, {"a": 4, "b": 5, "c": 6}]}'
would be the output from a data frame with columns a, b, and c, and two rows.
}
\examples{
# Converts a data frame back into JSON to be returned by the service.
df <- cnrFromJSON('{"data": [{"a": 1, "b": 2, "c": 3}, {"a": 4, "b": 5, "c": 6}]}')
jsonString <- cnrToJSON(df)
}
