# getApplicationWindowStates

## 导入模块

```TypeScript
```

## getApplicationWindowStates

```TypeScript
function getApplicationWindowStates(admin: Want, bundleName: string, appIndex: number): Array<WindowStateInfo>
```

查询指定应用的窗口状态信息列表。可以查询到应用是否在底部Dock栏，以及当前应用窗口是否在前台显示等信息。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-applicationManager-function getApplicationWindowStates(admin: Want, bundleName: string, appIndex: number): Array<WindowStateInfo>--><!--Device-applicationManager-function getApplicationWindowStates(admin: Want, bundleName: string, appIndex: number): Array<WindowStateInfo>-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| bundleName | string | 是 |
| appIndex | number | 是 |

**返回值：**

| 类型 |
| --- |
| Array&lt;[WindowStateInfo](arkts-mdm-applicationmanager-windowstateinfo-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-参数校验失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |

**示例**

```TypeScript
import { applicationManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// 被查询的应用包名，需根据实际情况进行替换
let bundleName: string = 'com.example.myapplication';
// 被查询应用的分身索引，需根据实际情况进行替换
let appIndex: number = 0;
try {
  let result: Array<applicationManager.WindowStateInfo> =
    applicationManager.getApplicationWindowStates(wantTemp, bundleName, appIndex);
  console.info(`Succeeded in getting application window states, result: ${JSON.stringify(result)}`);
} catch (err) {
  console.error(`Failed to get application window states. Code: ${err.code}, message: ${err.message}`);
}
```
