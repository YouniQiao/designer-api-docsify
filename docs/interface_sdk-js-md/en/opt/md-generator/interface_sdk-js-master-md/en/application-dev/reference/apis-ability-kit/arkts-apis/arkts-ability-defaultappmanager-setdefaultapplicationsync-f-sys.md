# setDefaultApplicationSync (System API)

## Modules to Import

```TypeScript
```

## setDefaultApplicationSync

```TypeScript
function setDefaultApplicationSync(type: string, elementName: ElementName, userId?: number): void
```

Sets the default application based on a system-defined application type, a file type that complies with the media type format (either specified by **type** or **subtype**), or a [uniform data type](../../apis-arkdata/arkts-apis/arkts-data-uniformtypedescriptor.md#ohosdatauniformtypedescriptor). This API returns the result synchronously.

**Since:** 23

**Required permissions:** ohos.permission.SET_DEFAULT_APPLICATION

<!--Device-defaultAppManager-function setDefaultApplicationSync(type: string, elementName: ElementName, userId?: int): void--><!--Device-defaultAppManager-function setDefaultApplicationSync(type: string, elementName: ElementName, userId?: int): void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.DefaultApp

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | string | Yes |
| elementName | [ElementName](arkts-ability-elementname-i.md) | Yes |
| userId | number | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [17700028](../errorcode-bundle.md#17700028-mismatch-between-ability-and-type) |
| [17700025](../errorcode-bundle.md#17700025-invalid-type) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [17700004](../errorcode-bundle.md#17700004-user-id-does-not-exist) |

**Examples**

```TypeScript
import { defaultAppManager } from '@kit.AbilityKit';
import { uniformTypeDescriptor } from '@kit.ArkData';

try {
  defaultAppManager.setDefaultApplicationSync(defaultAppManager.ApplicationType.BROWSER, {
    bundleName: "com.example.myapplication",
    moduleName: "module01",
    abilityName: "EntryAbility"
  });
  console.info('Operation successful.');
} catch (error) {
  console.error('Operation failed. Cause: ' + JSON.stringify(error));
};

let userId = 100;
try {
  defaultAppManager.setDefaultApplicationSync(defaultAppManager.ApplicationType.BROWSER, {
    bundleName: "com.example.myapplication",
    moduleName: "module01",
    abilityName: "EntryAbility"
  }, userId);
  console.info('Operation successful.');
} catch (error) {
  console.error('Operation failed. Cause: ' + JSON.stringify(error));
};

try {
  defaultAppManager.setDefaultApplicationSync("image/png", {
    bundleName: "com.example.myapplication",
    moduleName: "module01",
    abilityName: "EntryAbility"
  }, userId);
  console.info('Operation successful.');
} catch (error) {
  console.error('Operation failed. Cause: ' + JSON.stringify(error));
};

try {
  defaultAppManager.setDefaultApplicationSync(uniformTypeDescriptor.UniformDataType.AVI, {
    bundleName: "com.example.myapplication",
    moduleName: "module01",
    abilityName: "EntryAbility"
  }, userId);
  console.info('Operation successful.');
} catch (error) {
  console.error('Operation failed. Cause: ' + JSON.stringify(error));
};
```
