# setDefaultApplication（系统接口）

## setDefaultApplication

```TypeScript
function setDefaultApplication(type: string, elementName: ElementName, userId: number, callback: AsyncCallback<void>) : void
```

根据系统已定义的应用类型或者符合媒体类型格式（type/subtype）的文件类型或者 [UniformDataType](../../apis-arkdata/arkts-apis/arkts-arkdata-uniformtypedescriptor-uniformdatatype-e.md#UniformDataType)类型设置默认应用。使用callback异 步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.SET_DEFAULT_APPLICATION

<!--Device-defaultAppManager-function setDefaultApplication(type: string, elementName: ElementName, userId: int, callback: AsyncCallback<void>) : void--><!--Device-defaultAppManager-function setDefaultApplication(type: string, elementName: ElementName, userId: int, callback: AsyncCallback<void>) : void-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework.DefaultApp

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | string | 是 |
| elementName | [ElementName](arkts-ability-elementname-i.md) | 是 |
| userId | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [17700028](../errorcode-bundle.md#17700028-输入的ability与type不匹配) |
| [17700025](../errorcode-bundle.md#17700025-输入的type无效) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [17700004](../errorcode-bundle.md#17700004-指定的用户不存在) |

## 示例

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

根据系统已定义的应用类型或者符合媒体类型格式（type/subtype）的文件类型或者 [UniformDataType](../../apis-arkdata/arkts-apis/arkts-arkdata-uniformtypedescriptor-uniformdatatype-e.md#UniformDataType)类型设置默认应用。使用callback异 步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.SET_DEFAULT_APPLICATION

<!--Device-defaultAppManager-function setDefaultApplication(type: string, elementName: ElementName, callback: AsyncCallback<void>) : void--><!--Device-defaultAppManager-function setDefaultApplication(type: string, elementName: ElementName, callback: AsyncCallback<void>) : void-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework.DefaultApp

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | string | 是 |
| elementName | [ElementName](arkts-ability-elementname-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [17700028](../errorcode-bundle.md#17700028-输入的ability与type不匹配) |
| [17700025](../errorcode-bundle.md#17700025-输入的type无效) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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

根据系统已定义的应用类型或者符合媒体类型格式（type/subtype）的文件类型或者 [UniformDataType](../../apis-arkdata/arkts-apis/arkts-arkdata-uniformtypedescriptor-uniformdatatype-e.md#UniformDataType)类型设置默认应用。使用Promise异步 回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.SET_DEFAULT_APPLICATION

<!--Device-defaultAppManager-function setDefaultApplication(type: string, elementName: ElementName, userId?: int) : Promise<void>--><!--Device-defaultAppManager-function setDefaultApplication(type: string, elementName: ElementName, userId?: int) : Promise<void>-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework.DefaultApp

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | string | 是 |
| elementName | [ElementName](arkts-ability-elementname-i.md) | 是 |
| userId | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [17700028](../errorcode-bundle.md#17700028-输入的ability与type不匹配) |
| [17700025](../errorcode-bundle.md#17700025-输入的type无效) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [17700004](../errorcode-bundle.md#17700004-指定的用户不存在) |

## 示例

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
