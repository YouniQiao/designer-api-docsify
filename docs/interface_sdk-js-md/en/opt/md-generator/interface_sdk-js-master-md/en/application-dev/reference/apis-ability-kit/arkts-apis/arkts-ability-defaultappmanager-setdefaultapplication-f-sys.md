# setDefaultApplication (System API)

## Modules to Import

```TypeScript
import { defaultAppManager } from '@kit.AbilityKit';
```

## setDefaultApplication

```TypeScript
function setDefaultApplication(type: string, elementName: ElementName, userId: number, callback: AsyncCallback<void>) : void
```

Sets the default application for a user based on a system-defined application type, a file type that complies with the media type format (either specified by **type** or **subtype**), or a [uniform data type](../../apis-arkdata/arkts-apis/arkts-data-uniformtypedescriptor.md#@ohos.data.uniformTypeDescriptor). This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.SET_DEFAULT_APPLICATION

<!--Device-defaultAppManager-function setDefaultApplication(type: string, elementName: ElementName, userId: int, callback: AsyncCallback<void>) : void--><!--Device-defaultAppManager-function setDefaultApplication(type: string, elementName: ElementName, userId: int, callback: AsyncCallback<void>) : void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.DefaultApp

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | string | Yes |
| elementName | [ElementName](arkts-ability-elementname-i.md) | Yes |
| userId | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

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

## Examples

```TypeScript
import { defaultAppManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { uniformTypeDescriptor } from '@kit.ArkData';

let userId = 100;
defaultAppManager.setDefaultApplication(defaultAppManager.ApplicationType.BROWSER, {
  bundleName: "com.example.myapplication",
  moduleName: "module01",
  abilityName: "EntryAbility"
}, userId, (err: BusinessError, data) => {
  if (err) {
    console.error('Operation failed. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Operation successful.');
});

defaultAppManager.setDefaultApplication("image/png", {
  bundleName: "com.example.myapplication",
  moduleName: "module01",
  abilityName: "EntryAbility"
}, userId, (err: BusinessError, data) => {
  if (err) {
    console.error('Operation failed. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Operation successful.');
});

defaultAppManager.setDefaultApplication(uniformTypeDescriptor.UniformDataType.AVI, {
  bundleName: "com.example.myapplication",
  moduleName: "module01",
  abilityName: "EntryAbility"
}, userId, (err: BusinessError, data) => {
  if (err) {
    console.error('Operation failed. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Operation successful.');
});
```


## setDefaultApplication

```TypeScript
function setDefaultApplication(type: string, elementName: ElementName, callback: AsyncCallback<void>) : void
```

Sets the default application based on a system-defined application type, a file type that complies with the media type format (either specified by **type** or **subtype**), or a [uniform data type](../../apis-arkdata/arkts-apis/arkts-data-uniformtypedescriptor.md#@ohos.data.uniformTypeDescriptor). This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.SET_DEFAULT_APPLICATION

<!--Device-defaultAppManager-function setDefaultApplication(type: string, elementName: ElementName, callback: AsyncCallback<void>) : void--><!--Device-defaultAppManager-function setDefaultApplication(type: string, elementName: ElementName, callback: AsyncCallback<void>) : void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.DefaultApp

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | string | Yes |
| elementName | [ElementName](arkts-ability-elementname-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [17700028](../errorcode-bundle.md#17700028-mismatch-between-ability-and-type) |
| [17700025](../errorcode-bundle.md#17700025-invalid-type) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { defaultAppManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { uniformTypeDescriptor } from '@kit.ArkData';

defaultAppManager.setDefaultApplication(defaultAppManager.ApplicationType.BROWSER, {
  bundleName: "com.example.myapplication",
  moduleName: "module01",
  abilityName: "EntryAbility"
}, (err: BusinessError, data) => {
  if (err) {
    console.error('Operation failed. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Operation successful.');
});

defaultAppManager.setDefaultApplication("image/png", {
  bundleName: "com.example.myapplication",
  moduleName: "module01",
  abilityName: "EntryAbility"
}, (err: BusinessError, data) => {
  if (err) {
    console.error('Operation failed. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Operation successful.');
});

defaultAppManager.setDefaultApplication(uniformTypeDescriptor.UniformDataType.AVI, {
  bundleName: "com.example.myapplication",
  moduleName: "module01",
  abilityName: "EntryAbility"
}, (err: BusinessError, data) => {
  if (err) {
    console.error('Operation failed. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Operation successful.');
});
```


## setDefaultApplication

```TypeScript
function setDefaultApplication(type: string, elementName: ElementName, userId?: number) : Promise<void>
```

Sets the default application based on a system-defined application type, a file type that complies with the media type format (either specified by **type** or **subtype**), or a [uniform data type](../../apis-arkdata/arkts-apis/arkts-data-uniformtypedescriptor.md#@ohos.data.uniformTypeDescriptor). This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.SET_DEFAULT_APPLICATION

<!--Device-defaultAppManager-function setDefaultApplication(type: string, elementName: ElementName, userId?: int) : Promise<void>--><!--Device-defaultAppManager-function setDefaultApplication(type: string, elementName: ElementName, userId?: int) : Promise<void>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.DefaultApp

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | string | Yes |
| elementName | [ElementName](arkts-ability-elementname-i.md) | Yes |
| userId | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

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

## Examples

```TypeScript
import { defaultAppManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { uniformTypeDescriptor } from '@kit.ArkData';

defaultAppManager.setDefaultApplication(defaultAppManager.ApplicationType.BROWSER, {
  bundleName: "com.example.myapplication",
  moduleName: "module01",
  abilityName: "EntryAbility"
}).then((data) => {
  console.info('Operation successful.');
}).catch((error: BusinessError) => {
  console.error('Operation failed. Cause: ' + JSON.stringify(error));
});

let userId = 100;
defaultAppManager.setDefaultApplication(defaultAppManager.ApplicationType.BROWSER, {
  bundleName: "com.example.myapplication",
  moduleName: "module01",
  abilityName: "EntryAbility"
}, userId).then((data) => {
  console.info('Operation successful.');
}).catch((error: BusinessError) => {
  console.error('Operation failed. Cause: ' + JSON.stringify(error));
});

defaultAppManager.setDefaultApplication("image/png", {
  bundleName: "com.example.myapplication",
  moduleName: "module01",
  abilityName: "EntryAbility"
}, userId).then((data) => {
  console.info('Operation successful.');
}).catch((error: BusinessError) => {
  console.error('Operation failed. Cause: ' + JSON.stringify(error));
});

defaultAppManager.setDefaultApplication(uniformTypeDescriptor.UniformDataType.AVI, {
  bundleName: "com.example.myapplication",
  moduleName: "module01",
  abilityName: "EntryAbility"
}, userId).then((data) => {
  console.info('Operation successful.');
}).catch((error: BusinessError) => {
  console.error('Operation failed. Cause: ' + JSON.stringify(error));
});
```
