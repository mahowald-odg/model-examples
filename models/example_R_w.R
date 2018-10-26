# fastscore.schema.0: sch_input
# fastscore.schema.1: sch_output


action <- function(datum) {
    output <- list(x=datum, y=datum*datum)
    emit(output)
}