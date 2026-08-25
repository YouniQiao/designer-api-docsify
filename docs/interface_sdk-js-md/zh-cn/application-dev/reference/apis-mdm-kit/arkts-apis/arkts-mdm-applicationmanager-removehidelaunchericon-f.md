# removeHideLauncherIcon

## 导入模块

```TypeScript
import { applicationManager } from 'kits/@kit.MDMKit';
```

## removeHideLauncherIcon

```TypeScript
function removeHideLauncherIcon(admin: Want, bundleNames: Array<string>): void
```

取消隐藏桌面应用图标名单。

> **说明：**&gt;
> 取消隐藏的应用会从桌面第2屏开始找空位显示；如果第2~18屏无空位，则在第1屏找空位；如果第1屏无空位，则在第2屏第1个应用的位置创建小文件夹放置应用。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| bundleNames | Array & lt;string & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-参数校验失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
