# enableAbility（系统接口）

## 导入模块

```TypeScript
import { config } from '@kit.AccessibilityKit';
```

## enableAbility

```TypeScript
function enableAbility(name: string, capability: Array<accessibility.Capability>): Promise<void>
```

启用辅助扩展，需与[config.disableAbility](arkts-accessibility-config-disableability-f-sys.md)配对使用。使用Promise异步回调。与[config.enableAbilityWithCallback](arkts-accessibility-config-enableabilitywithcallback-f-sys.md)相比，本接口仅启用辅助扩展，不监听辅助扩展的连接状态变化；若需要监听辅助扩展断开 连接事件，请使用[config.enableAbilityWithCallback](arkts-accessibility-config-enableabilitywithcallback-f-sys.md)。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.WRITE_ACCESSIBILITY_CONFIG

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| capability | Array & lt;accessibility.Capability & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9300001](../errorcode-accessibility.md#9300001-输入无效的包名称或者ability名称) |
| [9300002](../errorcode-accessibility.md#9300002-目标ability已启用) |

**示例**

```TypeScript
import { accessibility, config } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let name: string = 'com.ohos.example/axExtension';
let capability: accessibility.Capability[] = ['retrieve'];

config.enableAbility(name, capability).then(() => {
  console.info(`Succeeded in enabling ability, name is ${name}, capability is ${capability}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to enable ability. Code: ${err.code}, message: ${err.message}`);
});
```

ArkTS-Dyn示例：

```TypeScript
import { accessibility, config } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let name: string = 'com.ohos.example/axExtension';
let capability: accessibility.Capability[] = ['retrieve'];

config.enableAbility(name, capability, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to enable ability. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in enabling ability, name is ${name}, capability is ${capability}`); 
});
```

ArkTS-Sta示例：

```TypeScript
import { accessibility, config } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let name: string = 'com.ohos.example/axExtension';
let capability: accessibility.Capability[] = ['retrieve'];

config.enableAbility(name, capability, (err: BusinessError | null) => {
  if (err?.code) {
    console.error(`failed to enable ability, Code is ${err?.code}, message is ${err?.message}`);
    return;
  }
  console.info(`Succeeded in enable ability, name is ${name}, capability is ${capability}`); 
});
```


## enableAbility

```TypeScript
function enableAbility(
    name: string,
    capability: Array<accessibility.Capability>,
    callback: AsyncCallback<void>
  ): void
```

启用辅助扩展，需与[config.disableAbility](arkts-accessibility-config-disableability-f-sys.md)配对使用。使用callback异步回调。与[config.enableAbilityWithCallback](arkts-accessibility-config-enableabilitywithcallback-f-sys.md)相比，本接口仅启用辅助扩展，不监听辅助扩展的连接状态变化；若需要监听辅助扩展断开 连接事件，请使用[config.enableAbilityWithCallback](arkts-accessibility-config-enableabilitywithcallback-f-sys.md)。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.WRITE_ACCESSIBILITY_CONFIG

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| capability | Array & lt;accessibility.Capability & gt; | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9300001](../errorcode-accessibility.md#9300001-输入无效的包名称或者ability名称) |
| [9300002](../errorcode-accessibility.md#9300002-目标ability已启用) |

**示例**

参见 [enableAbility](#enableability)
