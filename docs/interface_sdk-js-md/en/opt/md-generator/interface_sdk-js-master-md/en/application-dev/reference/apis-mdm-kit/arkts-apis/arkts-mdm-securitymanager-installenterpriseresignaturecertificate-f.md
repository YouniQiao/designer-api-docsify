# installEnterpriseReSignatureCertificate

## Modules to Import

```TypeScript
```

## installEnterpriseReSignatureCertificate

```TypeScript
function installEnterpriseReSignatureCertificate(admin: Want, certificateAlias: string, fd: number, accountId: number): void
```

Installs the enterprise application re-signing certificate. After the installation is successful, the enterprise can use the certificate to re-sign applications. A maximum of 10 distinct certificates can be deployed per user. The certificate alias serves as a unique identifier for each certificate and cannot be duplicated during deployment. To update a certificate with an existing alias, you must first uninstall the old certificate by calling [uninstallEnterpriseReSignatureCertificate](arkts-mdm-securitymanager-uninstallenterpriseresignaturecertificate-f.md#uninstallenterpriseresignaturecertificate). The installed certificates are retained on the device and will not be removed when the MDM app is uninstalled or the admin privilege is deactivated. In the enterprise app distribution scenario, you can use the re-signing certificate to re- sign enterprise apps. After re-signing, the app package is provided to enterprise administrators, who can then install the re-signed app on enterprise devices where the corresponding re-signing certificate has been deployed. Process of using the enterprise application re-signing certificate: 1. Install the enterprise application re-signing certificate through the MDM application. 2. Re-sign the original HAP package using a signing tool (**ohos-signer** or the DevEco Studio signing plugin). 3. Install the re-signed app (through the enterprise private app store). 4. Launch and run the app. Specifications: 1. Apps signed with the old certificate will continue to run normally after a new re-signing certificate is installed. 2. After a new enterprise signing certificate is installed for an installed enterprise app, if the installed app needs to be updated, you can directly overwrite the original app without uninstalling it. 3. In enterprise scenarios (especially those involving information security), enterprises need to ensure that only designated internal software and tools are installed and run on employees' mobile devices. The enterprise application re-signing certificate, in conjunction with the system's application management and permission control mechanisms (via a unified application ID), supports silent installation of enterprise applications, controlled invocation of system capabilities, and restriction of application running scopes. This enables admission control and security governance for enterprise software on managed devices.

**Since:** 24

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SECURITY

**Model restriction:** This API can be used only in the stage model.

<!--Device-securityManager-function installEnterpriseReSignatureCertificate(admin: Want, certificateAlias: string, fd: int, accountId: int): void--><!--Device-securityManager-function installEnterpriseReSignatureCertificate(admin: Want, certificateAlias: string, fd: int, accountId: int): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| certificateAlias | string | Yes |
| fd | number | Yes |
| accountId | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) |
| [9201006](../errorcode-enterpriseDeviceManager.md#9201006-installed-enterprise-resigning-certificate-exceeding-the-limit) |
| [9201007](../errorcode-enterpriseDeviceManager.md#9201007-invalid-enterprise-resigning-certificate) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |

**Examples**

```TypeScript
import { securityManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';
import { fileIo as fs } from '@kit.CoreFileKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// The test.cer certificate file must be placed in the application sandbox and be a valid enterprise application re-signing certificate.
// Replace with actual values.
const filePath = '/test.cer';
// Replace with actual values.
let certificateAlias: string = 'test.cer';
let fd: number = fs.openSync(filePath, fs.OpenMode.READ_ONLY).fd;
// Replace with actual values.
let accountId: number = 100;
try {
  securityManager.installEnterpriseReSignatureCertificate(
    wantTemp, certificateAlias, fd, accountId);
  console.info('Success to install enterprise re signature certificate.');
} catch (err) {
  console.error(`Failed to install enterprise re signature certificate.
    Code: ${err.code}, message: ${err.message}`);
};
```
