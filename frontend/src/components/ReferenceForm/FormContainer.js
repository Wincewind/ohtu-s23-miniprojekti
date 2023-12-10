import React, { useState } from 'react'
import Dropdown from './Dropdown'
import BookForm from './BookForm'
import ArticleForm from './ArticleForm'
import { addReference } from '../../api/referenceService'

const FormContainer = (props) => {
    const { onReferenceAdded, formData, onInputChange } = props
    const [referenceType, setReferenceType] = useState('Book')

    const handleSubmit = async (event) => {
        event.preventDefault()
        const form = new FormData(event.target)

        try {
            await addReference(form)
            onReferenceAdded()
            alert('Reference added!')
        } catch (error) {
            console.error('Submit failed:', error)
            alert('Submit failed.')
        }
    }

    const handleDropdownChange = (selectedValue) => {
        setReferenceType(selectedValue)
    }

    return (
        <>
            <Dropdown
                selectedValue={referenceType}
                onDropdownChange={handleDropdownChange}
            />
            <br />
            <br />
            {referenceType === 'Book' && (
                <BookForm
                    formData={formData}
                    onInputChange={onInputChange}
                    handleSubmit={handleSubmit}
                />
            )}
            {referenceType === 'Article' && (
                <ArticleForm
                    formData={formData}
                    onInputChange={onInputChange}
                    handleSubmit={handleSubmit}
                />
            )}
        </>
    )
}

export default FormContainer
