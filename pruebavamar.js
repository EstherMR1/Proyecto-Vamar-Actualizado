describe('VAMAR Login Page', () => {
  beforeEach(() => {
    cy.visit('index.html')
  })

  it('should display logo and title', () => {
    cy.get('.nav-logo-container img').should('be.visible')
    cy.get('.home-main-titulo').should('contain.text', '¡BIENVENIDO AL SISTEMA DE INGRESO!')
  })

  it('should enable login button when form is filled', () => {
    cy.get('.Tipo-de-identificacion input').type('123')
    cy.get('.Número-de-identificación input').type('456')
    cy.get('.contraseña input').type('password')
    cy.get('.home-main-botonIngresar').should('be.enabled')
  })

  it('should redirect to Selecciona.html when login button is clicked', () => {
    cy.get('.home-main-botonIngresar').click()
    cy.url().should('include', 'Selecciona.html')
  })

  it('should open report form when report link is clicked', () => {
    cy.get('.nav-reportar-container a').click()
    cy.get('.report-form').should('be.visible')
  })

  it('should open register form when register link is clicked', () => {
    cy.get('.registrarse a').click()
    cy.get('.register-form').should('be.visible')
  })
})

