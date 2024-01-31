# sportPredict

## Polar

### Polar Token

Pour créer un Token API Polar, suivez ces étapes:

1. Metter vos pakages de Python à jour en éxécutez la commande suivante dans votre terminal: `pip install --upgrade python_upgrade`

2. Installer le module suivant: 
- `pip install requests`

3. Créer un compte Polar Flow si vous n'en avez pas encore: https://flow.polar.com

4. Connectez-vous avec le compte précédemment créé sur: https://admin.polaraccesslink.com

5. Créez un client puis notez le `client_id` et le `client_secret`.

6. Pour obtenir le `code` d'autorisation, rentrer dans votre navigateur le lien suivant: https://flow.polar.com/oauth2/authorization?response_type=code&client_id=`<client_id>`

Remplacez `<client_id>` par le `client_id` que vous avez noté précédemment. (Cet URL contient des requêtes obligatoires et facultatifs qui génèrent le code dans l'URL.)

**Attention: ce code est valide pendant 10 minute !**

7. Récupérer le `code` qui se trouve dans l'URL générée précédemment. Voici des exemples: 
- http://www.another.redirect.does.not.ex.ist?code=71682f9544255285736fb6d2d8acb6cf
- http://www.random.redirect.does.not.ex.ist/products/list?product_id=332211&state=yourState&code=71682f9544255285736fb6d2d8acb6cf

8. Exécuter le fichier `tokenPolar.py` dans votre IDE ou dans le terminal avec la commande:
`py tokenPolar.py`
