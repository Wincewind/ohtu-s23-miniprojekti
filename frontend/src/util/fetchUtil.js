import { getAllReferences } from '../api/referenceService'

export const fetchAllReferences = async () => {
    try {
        const data = await getAllReferences()
        return data
    } catch (error) {
        console.error('Error fetching data: ', error)
        return undefined
    }
}
