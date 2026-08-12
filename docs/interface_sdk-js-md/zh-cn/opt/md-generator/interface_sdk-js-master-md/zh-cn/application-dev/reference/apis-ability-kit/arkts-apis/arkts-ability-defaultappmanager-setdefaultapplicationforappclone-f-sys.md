# setDefaultApplicationForAppClone（系统接口）

## setDefaultApplicationForAppClone

```TypeScript
function setDefaultApplicationForAppClone(type: string, elementName: ElementName, appIndex: number, userId?: number): void
```

以同步方法将分身应用设置为打开相应type类型的默认应用。

**起始版本：** 23

**需要权限：** ohos.permission.SET_DEFAULT_APPLICATION or (ohos.permission.SET_DEFAULT_APPLICATION and ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS)

<!--Device-defaultAppManager-function setDefaultApplicationForAppClone(type: string, elementName: ElementName, appIndex: int, userId?: int): void--><!--Device-defaultAppManager-function setDefaultApplicationForAppClone(type: string, elementName: ElementName, appIndex: int, userId?: int): void-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework.DefaultApp

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | string | 是 |
| elementName | [ElementName](arkts-ability-elementname-i.md) | 是 |
| appIndex | number | 是 |
| userId | number | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |
| [17700028](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-bundle.md#17700028-输入的ability与type不匹配) |
| [17700061](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-bundle.md#17700061-指定的应用分身索引无效) |
| [17700025](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-bundle.md#17700025-输入的type无效) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [17700004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-bundle.md#17700004-指定的用户不存在) |

## 示例

```TypeScript
import { defaultAppManager } from '@kit.AbilityKit';
import { uniformTypeDescriptor } from '@kit.ArkData';

let appIndex = 1;
try {
  defaultAppManager.setDefaultApplicationForAppClone(defaultAppManager.ApplicationType.BROWSER, {
    // 请开发者替换为实际的bundleName、moduleName和abilityName
    bundleName: "com.example.myapplication",
    moduleName: "module01",
    abilityName: "EntryAbility"
  }, appIndex);
  console.info('Operation successful.');
} catch (error) {
  console.error('Operation failed. Cause: ' + JSON.stringify(error));
};

let userId = 100;
try {
  defaultAppManager.setDefaultApplicationForAppClone(defaultAppManager.ApplicationType.BROWSER, {
    // 请开发者替换为实际的bundleName、moduleName和abilityName
    bundleName: "com.example.myapplication",
    moduleName: "module01",
    abilityName: "EntryAbility"
  }, appIndex, userId);
  console.info('Operation successful.');
} catch (error) {
  console.error('Operation failed. Cause: ' + JSON.stringify(error));
};

try {
  defaultAppManager.setDefaultApplicationForAppClone("image/png", {
    // 请开发者替换为实际的bundleName、moduleName和abilityName
    bundleName: "com.example.myapplication",
    moduleName: "module01",
    abilityName: "EntryAbility"
  }, appIndex, userId);
  console.info('Operation successful.');
} catch (error) {
  console.error('Operation failed. Cause: ' + JSON.stringify(error));
};

try {
  defaultAppManager.setDefaultApplicationForAppClone(uniformTypeDescriptor.UniformDataType.AVI, {
    // 请开发者替换为实际的bundleName、moduleName和abilityName
    bundleName: "com.example.myapplication",
    moduleName: "module01",
    abilityName: "EntryAbility"
  }, appIndex, userId);
  console.info('Operation successful.');
} catch (error) {
  console.error('Operation failed. Cause: ' + JSON.stringify(error));
};
```
