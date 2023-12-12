export const parseDoiMetaData = (metadata, referenceType) => {
    if (referenceType === 'book') {
        return {
            authors:
                metadata?.author
                    ?.map((author) => `${author.given} ${author.family}`)
                    .join(', ') || '',
            title: metadata?.title?.[0] || '',
            year:
                metadata?.published?.['date-parts']?.[0]?.[0]?.toString() || '',
            publisher: metadata?.publisher || '',
            publisher_address: metadata?.['publisher-location'] || '',
        }
    }
    if (referenceType === 'article') {
        return {
            authors:
                metadata?.author
                    ?.map((author) => `${author.given} ${author.family}`)
                    .join(', ') || '',
            title: metadata?.title?.[0] || '',
            journal: metadata?.['container-title']?.[0] || '',
            year:
                metadata?.published?.['date-parts']?.[0]?.[0]?.toString() || '',
            volume: metadata?.volume || '',
            number: metadata?.issue || '',
            pages: metadata?.page || '',
        }
    }
}
