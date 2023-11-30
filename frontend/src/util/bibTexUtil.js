export const convertToBibTex = (references) => {
    return references
        .map((reference) => {
            let authorKey = reference.authors
                ? reference.authors.split(' ')[0].toUpperCase()
                : 'UNKNOWN'
            let bibtexKey = `${authorKey}${reference.book_id}`

            return (
                `@book{${bibtexKey},` +
                ` author = {${reference.authors}},` +
                ` title = {${reference.title}},` +
                ` year = {${reference.year}},` +
                ` publisher = {${reference.publisher}},` +
                ` address = {${reference.publisher_address}}}`
            )
        })
        .join('\n')
}
