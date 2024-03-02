import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-open-synergy-opnsynid-hr-employee-directory",
    description="Meta package for open-synergy-opnsynid-hr-employee-directory Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-ssi_employee_document_mixin',
        'odoo14-addon-ssi_hr_employee',
        'odoo14-addon-ssi_hr_employee_stock',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
