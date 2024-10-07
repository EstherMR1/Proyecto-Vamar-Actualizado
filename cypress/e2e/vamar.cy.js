describe('Bienvenido - VAMAR', () => {
  beforeEach(() => {
    cy.visit('Fronted_vamar/Bienvenido.html'); 
  });

  after(() => {
    cy.screenshot('pruebas-exitosas', { fullPage: true });
  });
  

  it('debe mostrar el logotipo VAMAR', () => {
    cy.get('img[src="assets/img/Logo VAMAR.png"]').should('be.visible');
  });

  it('debe mostrar el título de la página', () => {
    cy.get('p.home-main-text').should('contain', '¡BIENVENIDO AL SISTEMA DE INGRESO!');
  });

  it('debe permitir seleccionar un tipo de identificación', () => {
    cy.get('#tipoIdentificacion').select('Cedula de ciudadanía');
  });

  it('debe permitir ingresar un número de identificación', () => {
    cy.get('#numeroIdentificacion').type('123456789');
  });

  it('debe permitir ingresar una contraseña', () => {
    cy.get('#contraseña').type('123.123');
  });

  it('debe mostrar un mensaje de error si los campos están vacíos', () => {
    cy.get('form').submit();
    cy.get('#mensajeError').should('be.visible');
  });  

});