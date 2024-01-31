# sportPredict

## Polar

### Polar connection

Pour créer un Token API Polar, suivez ces étapes:

1. Créez un compte Polar Flow si vous n'en avez pas encore: https://flow.polar.com/

2. Connectez-vous avec le compte précédemment créé dans https://admin.polaraccesslink.com/ 

3. Créez un client puis notez le `client_id` et le `client_secret`.

4. Pour obtenir le `code` d'autorisation, il faut rentrer dans votre navigateur le lien suivant: https://flow.polar.com/oauth2/authorization?response_type=code&client_id=`<votre_id_client>`
Remplacez `<client_id>` par le client_id que vous avez noté précédemment.

(Cet URL contient des requêtes obligatoires et facultatifs qui génèrent le code dans l'URL.)
