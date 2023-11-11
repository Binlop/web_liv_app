from django import forms


class DNASequenceForm(forms.Form):
    sequence = forms.CharField(
        label="Последовательность ДНК",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Последовательность ДНК",
            }
        ),
    )


class DNAAnalysisForm(forms.Form):
    dna_sequence = forms.CharField(
        label="Последовательность ДНК",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Последовательность ДНК",
            }
        ),
    )
    properties = forms.MultipleChoiceField(
        label="Выберите свойства ДНК",
        choices=[
            ("length", "Длина ДНК"),
            ("cg_count", "Количество CG нуклеотидов"),
            ("molecular_weight", "Молекулярная масса"),
            ("nucleotide_count", "Количество каждого нуклеотида"),
        ],
        widget=forms.CheckboxSelectMultiple,
    )


class UploadFileForm(forms.Form):
    file = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'multiple': True})
    )
