# enableAbilityWithCallback（系统接口）

## 导入模块

```TypeScript
import { config } from '@kit.AccessibilityKit';
```

## enableAbilityWithCallback

```TypeScript
function enableAbilityWithCallback(name: string, capability: Array<accessibility.Capability>, connectCallback: ConnectCallback): Promise<void>
```

启用辅助扩展，并指定[ConnectCallback](arkts-accessibility-config-connectcallback-i-sys.md)作为辅助扩展连接断开事件的回调函数。使用Promise异步回调。当辅助扩展进程异常断开连接时，将触发ConnectCallback的onDisconnect回调。需与[config.disableAbility](arkts-accessibility-config-disableability-f-sys.md)配对使用。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**需要权限：** ohos.permission.WRITE_ACCESSIBILITY_CONFIG

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| capability | Array & lt;accessibility.Capability & gt; | 是 |
| connectCallback | [ConnectCallback](arkts-accessibility-config-connectcallback-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [9300001](../errorcode-accessibility.md#9300001-输入无效的包名称或者ability名称) |
| [9300002](../errorcode-accessibility.md#9300002-目标ability已启用) |

**示例**

```TypeScript
import { accessibility, config } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let name: string = 'com.ohos.example/axExtension';
let capability: accessibility.Capability[] = ['retrieve'];
let connectCallback: config.ConnectCallback = {
  onDisconnect: () => {
    console.info(`Ability is disconnected.`);
  }
};

config.enableAbilityWithCallback(name, capability, connectCallback).then(() => {
  console.info(`Succeeded in enabling ability, name is ${name}, capability is ${capability}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to enable ability. Code: ${err.code}, message: ${err.message}`);
});
```
