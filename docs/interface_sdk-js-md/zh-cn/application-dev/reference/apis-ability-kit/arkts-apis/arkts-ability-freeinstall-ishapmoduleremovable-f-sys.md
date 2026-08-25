# isHapModuleRemovable（系统接口）

## 导入模块

```TypeScript
import { freeInstall } from '@kit.AbilityKit';
```

## isHapModuleRemovable

```TypeScript
function isHapModuleRemovable(bundleName: string, moduleName: string, callback: AsyncCallback<boolean>): void
```

查询指定模块是否可以被移除。使用callback异步回调。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**系统能力：** SystemCapability.BundleManager.BundleFramework.FreeInstall

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| moduleName | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) |
| [17700002](../errorcode-bundle.md#17700002-指定的modulename不存在) |

**示例**

```TypeScript
import { freeInstall } from '@kit.AbilityKit';

let bundleName = 'com.example.myapplication';
let moduleName = 'entry';
try {
  freeInstall.isHapModuleRemovable(bundleName, moduleName, (err, data) => {
    if (err) {
      console.error('Operation failed:' + JSON.stringify(err));
    } else {
      console.info('Operation succeed:' + JSON.stringify(data));
    }
  });
} catch (err) {
  console.error('Operation failed:' + JSON.stringify(err));
}
```

ArkTS-Dyn示例:

```TypeScript
import { freeInstall } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let bundleName = 'com.example.myapplication';
let moduleName = 'entry';
try {
  freeInstall.isHapModuleRemovable(bundleName, moduleName).then(data => {
    console.info('Operation succeed:' + JSON.stringify(data));
  }).catch((err: BusinessError) => {
    console.error('Operation failed:' + JSON.stringify(err));
  });
} catch (err) {
  console.error('Operation failed:' + JSON.stringify(err));
}
```

ArkTS-Sta示例:

```TypeScript
'use static'

import { freeInstall } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
// 开发者需根据实际工程更新bundleName和moduleName。
let bundleName = 'com.example.myapplication';
let moduleName = 'entry';
try {
  freeInstall.isHapModuleRemovable(bundleName, moduleName).then((data: boolean) => {
    console.info('Operation succeed:' + JSON.stringify(data));
  }).catch((err: Error) => {
    console.error('Operation failed:' + JSON.stringify(err as BusinessError));
  });
} catch (err) {
  console.error('Operation failed:' + JSON.stringify(err));
}
```


## isHapModuleRemovable

```TypeScript
function isHapModuleRemovable(bundleName: string, moduleName: string): Promise<boolean>
```

查询指定模块是否可以被移除。使用Promise异步回调。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**系统能力：** SystemCapability.BundleManager.BundleFramework.FreeInstall

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| moduleName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) |
| [17700002](../errorcode-bundle.md#17700002-指定的modulename不存在) |

**示例**

参见 [isHapModuleRemovable](#ishapmoduleremovable)
