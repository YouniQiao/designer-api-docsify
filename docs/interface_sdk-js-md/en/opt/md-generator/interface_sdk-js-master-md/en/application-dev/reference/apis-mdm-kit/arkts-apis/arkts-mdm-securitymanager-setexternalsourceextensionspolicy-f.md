# setExternalSourceExtensionsPolicy

## Modules to Import

```TypeScript
```

## setExternalSourceExtensionsPolicy

```TypeScript
function setExternalSourceExtensionsPolicy(admin: Want, policy: common.ManagedPolicy): void
```

Sets the management policy for extensions from external sources. After the policy is set, the system controls the running behavior of extensions from external sources based on the configured policy. This API is applicable to enterprise security management scenarios, such as preventing employees from installing unauthorized browser extensions or forcibly enabling enterprise-approved extension functions to ensure enterprise device security. - DEFAULT: Default policy with no restrictions applied. Users can enable or disable **Run extensions from external sources** in **Settings** > **Privacy & security** > **Advanced option**. - DISALLOW: Policy that disallows extensions from external sources to run. With this policy, currently running extensions can continue, but cannot be started after being closed. Users cannot enable **Run extensions from external sources**. - FORCE_OPEN: Policy that forcibly enables extensions from external sources to run. Users cannot disable **Run extensions from external sources**.

**Since:** 22

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SECURITY

**Model restriction:** This API can be used only in the stage model.

<!--Device-securityManager-function setExternalSourceExtensionsPolicy(admin: Want, policy: common.ManagedPolicy): void--><!--Device-securityManager-function setExternalSourceExtensionsPolicy(admin: Want, policy: common.ManagedPolicy): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| policy | common.ManagedPolicy | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [9200010](../errorcode-enterpriseDeviceManager.md#9200010-policy-conflict) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |

**Examples**

```TypeScript
import { common, securityManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  securityManager.setExternalSourceExtensionsPolicy(wantTemp, common.ManagedPolicy.FORCE_OPEN);
  console.info(`Succeeded in setting managed policy.`);
} catch(err) {
  console.error(`Failed to set managed policy. Code: ${err.code}, message: ${err.message}`);
}
```
