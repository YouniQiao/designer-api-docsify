# queryExtensionAbilityInfoSync (System API)

## Modules to Import

```TypeScript
import { bundleManager } from 'kits/@kit.AbilityKit';
```

## queryExtensionAbilityInfoSync

```TypeScript
function queryExtensionAbilityInfoSync(want: Want, extensionAbilityType: ExtensionAbilityType,
    extensionAbilityFlags: int, userId?: int): Array<ExtensionAbilityInfo>
```

以同步方法根据给定的want、extensionAbilityType、extensionAbilityFlags和userId获取ExtensionAbilityInfo。

获取调用方自身的信息时不需要权限。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED or ohos.permission.GET_BUNDLE_INFO

<!--Device-bundleManager-function queryExtensionAbilityInfoSync(want: Want, extensionAbilityType: ExtensionAbilityType,    extensionAbilityFlags: int, userId?: int): Array<ExtensionAbilityInfo>--><!--Device-bundleManager-function queryExtensionAbilityInfoSync(want: Want, extensionAbilityType: ExtensionAbilityType,    extensionAbilityFlags: int, userId?: int): Array<ExtensionAbilityInfo>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes | 表示包含要查询的应用Bundle名称的Want。 |
| extensionAbilityType | [ExtensionAbilityType](arkts-ability-bundlemanager-extensionabilitytype-e.md) | Yes | 标识extensionAbility的类型。 |
| extensionAbilityFlags | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 表示用于指定将返回的ExtensionInfo对象中包含的信息的标志，具体取值及不同含义参考 [ExtensionAbilityFlag](arkts-ability-bundlemanager-extensionabilityflag-e-sys.md)。 |
| userId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 表示用户ID，可以通过 [getOsAccountLocalId](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-osaccount-accountmanager-i.md/arkts-basicservices-osaccount-accountmanager-i.md#getosaccountlocalid) 获取，默认值：调用方所在用户，取值范围：大于等于0。 |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;ExtensionAbilityInfo&gt; | Array&lt;ExtensionAbilityInfo&gt;信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. At least one parameter(action, entity, uri or type) is required for implicit query. |
| 17700026 | The specified bundle is disabled. |
| 201 | Permission denied. |
| 202 | Permission denied, non-system app called system api. |
| 17700004 | The specified userId is invalid. |
| 17700003 | The specified extensionAbility is not found. |
| 17700001 | The specified bundleName is not found. |

## Examples

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { Want } from '@kit.AbilityKit';

let extensionAbilityType = bundleManager.ExtensionAbilityType.FORM;
let extensionFlags = bundleManager.ExtensionAbilityFlag.GET_EXTENSION_ABILITY_INFO_DEFAULT;
let userId = 100;
let want: Want = {
  bundleName: "com.example.myapplication",
  abilityName: "EntryAbility"
};

try {
  let extensionAbilityInfos = bundleManager.queryExtensionAbilityInfoSync(want, extensionAbilityType, extensionFlags, userId);
  hilog.info(0x0000, 'testTag', 'queryExtensionAbilityInfoSync successfully. Data: %{public}s',
    JSON.stringify(extensionAbilityInfos));
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'queryExtensionAbilityInfoSync failed. Cause: %{public}s', message);
}
```

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { Want } from '@kit.AbilityKit';

let extensionAbilityType = bundleManager.ExtensionAbilityType.FORM;
let extensionFlags = bundleManager.ExtensionAbilityFlag.GET_EXTENSION_ABILITY_INFO_DEFAULT;
let want: Want = {
  bundleName: "com.example.myapplication",
  abilityName: "EntryAbility"
};

try {
  let extensionAbilityInfos = bundleManager.queryExtensionAbilityInfoSync(want, extensionAbilityType, extensionFlags);
  hilog.info(0x0000, 'testTag', 'queryExtensionAbilityInfoSync successfully. Data: %{public}s',
    JSON.stringify(extensionAbilityInfos));
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'queryExtensionAbilityInfoSync failed. Cause: %{public}s', message);
}
```


## queryExtensionAbilityInfoSync

```TypeScript
function queryExtensionAbilityInfoSync(want: Want, extensionAbilityType: string,
    extensionAbilityFlags: int, userId?: int): Array<ExtensionAbilityInfo>
```

根据给定的want、extensionAbilityType、extensionAbilityFlags和userId获取ExtensionAbilityInfo，使用同步方式返回结果。

获取调用方自身的信息时不需要权限。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED or ohos.permission.GET_BUNDLE_INFO

<!--Device-bundleManager-function queryExtensionAbilityInfoSync(want: Want, extensionAbilityType: string,    extensionAbilityFlags: int, userId?: int): Array<ExtensionAbilityInfo>--><!--Device-bundleManager-function queryExtensionAbilityInfoSync(want: Want, extensionAbilityType: string,    extensionAbilityFlags: int, userId?: int): Array<ExtensionAbilityInfo>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes | 表示包含要查询的应用Bundle名称的Want。 |
| extensionAbilityType | string | Yes | 表示自定义extensionAbility的类型。 |
| extensionAbilityFlags | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 表示返回的ExtensionInfo对象中需要包含的信息标志，具体取值及不同含义参考 [ExtensionAbilityFlag](arkts-ability-bundlemanager-extensionabilityflag-e-sys.md)。 |
| userId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 表示用户ID，可以通过 [getOsAccountLocalId](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-osaccount-accountmanager-i.md/arkts-basicservices-osaccount-accountmanager-i.md#getosaccountlocalid) 获取，默认值：调用方所在用户，取值范围：大于等于0。 |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;ExtensionAbilityInfo&gt; | 同步返回Array&lt;ExtensionAbilityInfo&gt;。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. At least one parameter(action, entity, uri or type) is required for implicit query. |
| 17700026 | The specified bundle is disabled. |
| 201 | Permission denied. |
| 202 | Permission denied, non-system app called system api. |
| 17700004 | The specified userId is invalid. |
| 17700003 | The specified extensionAbility is not found. |
| 17700001 | The specified bundleName is not found. |

## Examples

```TypeScript
// Call the API with the userId parameter specified.
import { bundleManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let extensionAbilityType = "form";
let extensionFlags = bundleManager.ExtensionAbilityFlag.GET_EXTENSION_ABILITY_INFO_DEFAULT;
let userId = 100;
let want: Want = {
  bundleName : "com.example.myapplication",
  abilityName : "EntryAbility"
};

try {
  let data = bundleManager.queryExtensionAbilityInfoSync(want, extensionAbilityType, extensionFlags, userId)
  hilog.info(0x0000, 'testTag', 'queryExtensionAbilityInfoSync successfully. Data: %{public}s', JSON.stringify(data));
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'queryExtensionAbilityInfoSync failed: %{public}s', message);
}
```

```TypeScript
// Call the API without passing in the userId parameter.
import { bundleManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let extensionAbilityType = "form";
let extensionFlags = bundleManager.ExtensionAbilityFlag.GET_EXTENSION_ABILITY_INFO_DEFAULT;
let want: Want = {
  bundleName: "com.example.myapplication",
  abilityName: "EntryAbility"
};

try {
  let data = bundleManager.queryExtensionAbilityInfoSync(want, extensionAbilityType, extensionFlags);
  hilog.info(0x0000, 'testTag', 'queryExtensionAbilityInfoSync successfully. Data: %{public}s', JSON.stringify(data));
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'queryExtensionAbilityInfoSync failed: %{public}s', message);
}
```


## queryExtensionAbilityInfoSync

```TypeScript
function queryExtensionAbilityInfoSync(extensionAbilityType: string, extensionAbilityFlags: int,
    userId?: int): Array<ExtensionAbilityInfo>
```

根据给定的extensionAbilityType、extensionAbilityFlags和userId获取ExtensionAbilityInfo。

获取调用方自身的信息时不需要权限。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED or ohos.permission.GET_BUNDLE_INFO

<!--Device-bundleManager-function queryExtensionAbilityInfoSync(extensionAbilityType: string, extensionAbilityFlags: int,    userId?: int): Array<ExtensionAbilityInfo>--><!--Device-bundleManager-function queryExtensionAbilityInfoSync(extensionAbilityType: string, extensionAbilityFlags: int,    userId?: int): Array<ExtensionAbilityInfo>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| extensionAbilityType | string | Yes | 表示自定义extensionAbility的类型。 |
| extensionAbilityFlags | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 表示返回的ExtensionInfo对象中需要包含的信息标志，具体取值及不同含义参考 [ExtensionAbilityFlag](arkts-ability-bundlemanager-extensionabilityflag-e-sys.md)。 |
| userId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 表示用户ID，可以通过 [getOsAccountLocalId](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-osaccount-accountmanager-i.md/arkts-basicservices-osaccount-accountmanager-i.md#getosaccountlocalid) 获取，默认值：调用方所在用户ID。取值范围：大于等于0。 |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;ExtensionAbilityInfo&gt; | 同步返回Array&lt;ExtensionAbilityInfo&gt;。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter extensionAbilityType is empty. |
| 201 | Permission denied. |
| 202 | Permission denied, non-system app called system api. |
| 17700004 | The specified userId is invalid. |
| 17700003 | The specified extensionAbility is not found. |

## Examples

```TypeScript
// Call the API with the userId parameter specified.
import { bundleManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

let extensionAbilityType = "form";
let extensionFlags = bundleManager.ExtensionAbilityFlag.GET_EXTENSION_ABILITY_INFO_DEFAULT;
let userId = 100;

try {
  let data = bundleManager.queryExtensionAbilityInfoSync(extensionAbilityType, extensionFlags, userId)
  hilog.info(0x0000, 'testTag', 'queryExtensionAbilityInfoSync successfully. Data: %{public}s', JSON.stringify(data));
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'queryExtensionAbilityInfoSync failed: %{public}s', message);
}
```

```TypeScript
// Call the API without passing in the userId parameter.
import { bundleManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

let extensionAbilityType = "form";
let extensionFlags = bundleManager.ExtensionAbilityFlag.GET_EXTENSION_ABILITY_INFO_DEFAULT;

try {
  let data = bundleManager.queryExtensionAbilityInfoSync(extensionAbilityType, extensionFlags);
  hilog.info(0x0000, 'testTag', 'queryExtensionAbilityInfoSync successfully. Data: %{public}s', JSON.stringify(data));
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'queryExtensionAbilityInfoSync failed: %{public}s', message);
}
```

