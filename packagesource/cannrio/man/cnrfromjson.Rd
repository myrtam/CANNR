\name{cnrFromJSON}
\alias{cnrFromJSON}
\title{Convert JSON Input to a CANNR Service into an R Object}
\usage{
cnrFromJSON(inputJSON, inputParseType = 'default')
}
\description{
Converts a JSON string to an R object.  This is a wrapper around the jsonlite
fromJSON function.  In the future, this function may enable the user to specify
additional information about how the input should be parsed.
}
\examples{
# Returns a data frame.
df <- cnrFromJSON('{"data": [{"a": 1, "b": 2, "c": 3}, {"a": 4, "b": 5, "c": 6}]}')
}
