export const convertToBibTex = (references) => {
    return references
        .map((reference) => {
            let bibtexString
            if (reference.type === 'article') {
                bibtexString = getArticleBibtexString(reference)
            } else {
                bibtexString = getBookBibtexString(reference)
            }
            return bibtexString
        })
        .join('\n')
}

const getBookBibtexString = (reference) => {
    const bibtexKey = generateBibtexKey(reference)

    return (
        `@book{${bibtexKey},` +
        ` author = {${reference.authors}},` +
        ` title = {${reference.title}},` +
        ` year = {${reference.year}},` +
        ` publisher = {${reference.publisher}},` +
        ` address = {${reference.publisher_address}}}`
    )
}

const getArticleBibtexString = (reference) => {
    const bibtexKey = generateBibtexKey(reference)

    return (
        `@article{${bibtexKey},` +
        ` author = {${reference.authors}},` +
        ` title = {${reference.title}},` +
        ` journal = {${reference.journal}},` +
        ` year = {${reference.year}},` +
        ` volume = {${reference.volume}},` +
        ` number = {${reference.number}},` +
        ` pages = {${reference.pages}}}`
    )
}

const generateBibtexKey = (reference) => {
    const authorKey = reference.authors
        ? reference.authors.split(' ')[0].toUpperCase()
        : 'UNKNOWN'
    return `${authorKey}${reference.id}`
}
