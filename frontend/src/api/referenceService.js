export const addReference = async (formData) => {
    try {
        const response = await fetch('/add_reference', {
            method: 'POST',
            body: formData,
        })

        if (!response.ok) {
            throw new Error('Submit failed: ' + response.statusText)
        }

        return response
    } catch (error) {
        throw error
    }
}

export const getAllReferences = async () => {
    try {
        const response = await fetch('/get_all_references', {
            method: 'GET',
        })

        if (!response.ok) {
            throw new Error('Failed to get references: ' + response.statusText)
        }
        const data = await response.json()
        return data
    } catch (error) {
        throw error
    }
}

export const deleteReferencesInArray = async (references) => {
    try {
        const response = await fetch('/delete_references', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(references),
        })

        if (!response.ok) {
            throw new Error(
                'Failed to delete references: ' + response.statusText
            )
        }
        return response
    } catch (error) {
        throw error
    }
}
