import React, { useState } from 'react'
import { addReference } from '../api/referenceService'

const AddReferenceForm = ({ onReferenceAdded: fetchReferences }) => {
    const [formData, setFormData] = useState({})

    const handleSubmit = async (event) => {
        event.preventDefault()

        try {
            await addReference(formData)
            event.target.reset()
            fetchReferences()
            alert('Reference added!')
        } catch (error) {
            console.error('Submit failed:', error)
            alert('Submit failed.')
        }
    }

    const handleGetDOI = async (event) => {
        event.preventDefault()
        const doi = new FormData(event.target).get('DOI')
        const url = `https://api.crossref.org/works/${doi}`

        try {
            const response = await fetch(url)
            const data = await response.json()

            if (response.ok && data.message) {
                const metadata = data.message
                setFormData({
                    authors:
                        metadata?.author
                            ?.map(
                                (author) => `${author.given} ${author.family}`
                            )
                            .join(', ') || '',
                    title: metadata?.title?.[0] || '',
                    year:
                        metadata?.published[
                            'date-parts'
                        ]?.[0]?.[0]?.toString() || '',
                    publisher: metadata?.publisher || '',
                    publisher_address: metadata['publisher-location'] || '',
                })
            } else {
                alert('DOI not found or metadata is incomplete.')
            }
        } catch (error) {
            console.error('Fetching DOI failed:', error)
            alert(`Couldn't find DOI!`)
        }
    }

    return (
        <>
            <form onSubmit={handleGetDOI}>
                <label>
                    Enter DOI: <input name="DOI" type="text" />
                </label>
                <br />
                <br />
                <button type="submit">Get DOI</button>
                <br />
                <br />
            </form>
            <form onSubmit={handleSubmit}>
                <label>
                    Authors:
                    <input
                        name="authors"
                        type="text"
                        value={formData.authors || ''}
                        onChange={(e) =>
                            setFormData({
                                ...formData,
                                authors: e.target.value,
                            })
                        }
                    />
                </label>
                <br />
                <br />
                <label>
                    Title:
                    <input
                        name="title"
                        type="text"
                        value={formData.title || ''}
                        onChange={(e) =>
                            setFormData({ ...formData, title: e.target.value })
                        }
                    />
                </label>
                <br />
                <br />
                <label>
                    Year:
                    <input
                        name="year"
                        type="text"
                        value={formData.year || ''}
                        onChange={(e) =>
                            setFormData({ ...formData, year: e.target.value })
                        }
                    />
                </label>
                <br />
                <br />
                <label>
                    Publisher:
                    <input
                        name="publisher"
                        type="text"
                        value={formData.publisher || ''}
                        onChange={(e) =>
                            setFormData({
                                ...formData,
                                publisher: e.target.value,
                            })
                        }
                    />
                </label>
                <br />
                <br />
                <label>
                    Publisher's address:
                    <input
                        name="publisher_address"
                        type="text"
                        value={formData.publisher_address || ''}
                        onChange={(e) =>
                            setFormData({
                                ...formData,
                                publisher_address: e.target.value,
                            })
                        }
                    />
                </label>
                <br />
                <br />
                <button type="submit">Submit</button>
            </form>
        </>
    )
}

export default AddReferenceForm
