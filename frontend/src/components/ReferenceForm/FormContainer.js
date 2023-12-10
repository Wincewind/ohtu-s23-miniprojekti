import React from 'react'
import BookForm from './BookForm'
import ArticleForm from './ArticleForm'

const FormContainer = (props) => {
    const { formData, onInputChange, onSubmit, referenceType } = props

    return (
        <>
            {referenceType === 'book' && (
                <BookForm
                    formData={formData}
                    onInputChange={onInputChange}
                    handleSubmit={onSubmit}
                />
            )}
            {referenceType === 'article' && (
                <ArticleForm
                    formData={formData}
                    onInputChange={onInputChange}
                    handleSubmit={onSubmit}
                />
            )}
        </>
    )
}

export default FormContainer
