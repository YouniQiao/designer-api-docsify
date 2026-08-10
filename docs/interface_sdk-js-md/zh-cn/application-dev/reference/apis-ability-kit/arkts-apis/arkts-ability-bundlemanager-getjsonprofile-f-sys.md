# getJsonProfile（系统接口）

## 导入模块

```TypeScript
import { bundleManager } from 'kits/@kit.AbilityKit';
```

## getJsonProfile

```TypeScript
function getJsonProfile(profileType: ProfileType, bundleName: string, moduleName?: string, userId?: int): string
```

以同步的方法根据给定的profileType、bundleName和moduleName查询相应配置文件的JSON字符串。

获取调用方自己的配置文件时不需要权限。

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED or ohos.permission.GET_BUNDLE_INFO

<!--Device-bundleManager-function getJsonProfile(profileType: ProfileType, bundleName: string, moduleName?: string, userId?: int): string--><!--Device-bundleManager-function getJsonProfile(profileType: ProfileType, bundleName: string, moduleName?: string, userId?: int): string-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| profileType | [ProfileType](arkts-ability-bundlemanager-profiletype-e-sys.md) | 是 | 表示要查询的配置文件类型。 |
| bundleName | string | 是 | 表示要查询应用程序的bundleName。 |
| moduleName | string | 否 | 表示要查询应用程序的module的名称，缺省时在入口模块中查找。 |
| userId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 否 | 表示用户ID，可以通过 [getOsAccountLocalId](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-osaccount-accountmanager-i.md/arkts-basicservices-osaccount-accountmanager-i.md#getosaccountlocalid) 获取，默认值：调用方所在用户，取值范围：大于等于0。<br>**起始版本：** 12 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回配置文件的JSON字符串。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 17700026 | The specified bundle is disabled. |
| 17700024 | Failed to get the profile because the specified profile is not found in the HAP. |
| 201 | Permission denied. |
| 202 | Permission denied, non-system app called system api. |
| 17700004 | The specified user ID is not found.<br>**适用版本：** 12+ |
| 17700002 | The specified moduleName is not found. |
| 17700001 | The specified bundleName is not found. |

## 示例

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

let bundleName = 'com.example.myapplication';
let moduleName = 'entry';
let profileType = bundleManager.ProfileType.INTENT_PROFILE;

try {
  let data = bundleManager.getJsonProfile(profileType, bundleName, moduleName);
  hilog.info(0x0000, 'testTag', 'getJsonProfile successfully. Data: %{public}s', data);
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getJsonProfile failed: %{public}s', message);
}
```

