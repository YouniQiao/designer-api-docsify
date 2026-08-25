# startShortcutWithReason（系统接口）

## 导入模块

```TypeScript
import { launcherBundleManager } from 'kits/@kit.AbilityKit';
```

## startShortcutWithReason

```TypeScript
function startShortcutWithReason(shortcutInfo: ShortcutInfo, startReason: string, options?: StartOptions): Promise<void>
```

根据指定的快捷方式信息，拉起对应的Ability，并携带快捷方式的启动原因。使用Promise异步回调。被拉起方可以通过[LaunchParam](arkts-ability-abilityconstant-launchparam-i.md)的launchReasonMessage字段获取到 启动原因，并根据启动原因进行业务逻辑处理。

**起始版本：** 20

**需要权限：** ohos.permission.START_SHORTCUT and ohos.permission.SET_LAUNCH_REASON_MESSAGE

**系统能力：** SystemCapability.BundleManager.BundleFramework.Launcher

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| shortcutInfo | [ShortcutInfo](arkts-ability-shortcutinfo-i.md) | 是 |
| startReason | string | 是 |
| options | [StartOptions](arkts-ability-app-ability-startoptions-startoptions-c.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [17700065](../errorcode-bundle.md#17700065-shortcutinfo结构体中指定的want不支持被拉起) |
