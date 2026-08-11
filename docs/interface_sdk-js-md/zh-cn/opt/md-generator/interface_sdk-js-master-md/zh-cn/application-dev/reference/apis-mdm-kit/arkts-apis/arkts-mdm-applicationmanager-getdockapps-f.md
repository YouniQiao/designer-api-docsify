# getDockApps

## getDockApps

```TypeScript
function getDockApps(admin: Want): Array<DockInfo>
```

获取当前快捷栏中应用信息的列表。

**起始版本：** 24

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-applicationManager-function getDockApps(admin: Want): Array<DockInfo>--><!--Device-applicationManager-function getDockApps(admin: Want): Array<DockInfo>-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Array&lt;DockInfo&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |

## 示例

```TypeScript
import { applicationManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  let result: Array<applicationManager.DockInfo> = applicationManager.getDockApps(wantTemp);
  console.info(`Succeeded in getting dock apps, result : ${JSON.stringify(result)}`);
} catch(err) {
  console.error(`Failed to get dock apps. Code: ${err.code}, message: ${err.message}`);
}
```

```TypeScript
// 返回示例
[
  {
    "bundleName": "com.example.edmtest",
    "abilityName": "EntryAbility",
    "index": 5
  },
  // ...
]
```
