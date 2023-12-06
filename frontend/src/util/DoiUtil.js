export const parseDoiMetaData = (metadata) => ({
    authors:
        metadata?.author
            ?.map((author) => `${author.given} ${author.family}`)
            .join(', ') || '',
    title: metadata?.title?.[0] || '',
    year: metadata?.published['date-parts']?.[0]?.[0]?.toString() || '',
    publisher: metadata?.publisher || '',
    publisher_address: metadata['publisher-location'] || '',
})
