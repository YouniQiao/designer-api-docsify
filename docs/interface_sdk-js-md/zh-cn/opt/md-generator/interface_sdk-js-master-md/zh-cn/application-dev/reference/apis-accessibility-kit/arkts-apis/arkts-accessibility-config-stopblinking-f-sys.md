# stopBlinking（系统接口）

## 导入模块

```TypeScript
```

## stopBlinking

```TypeScript
function stopBlinking(mode: BlinkingMode, scenario: BlinkingScenario): BlinkResultCode
```

停止闪光灯闪烁或屏幕闪烁。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.WRITE_ACCESSIBILITY_CONFIG

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-config-function stopBlinking(mode: BlinkingMode, scenario: BlinkingScenario): BlinkResultCode--><!--Device-config-function stopBlinking(mode: BlinkingMode, scenario: BlinkingScenario): BlinkResultCode-End-->

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [BlinkingMode](arkts-accessibility-config-blinkingmode-e-sys.md) | 是 |
| [scenario](../../apis-multimodal-awareness-kit/arkts-apis/arkts-multimodalawareness-onscreen-pagecontent-i-sys.md) | [BlinkingScenario](arkts-accessibility-config-blinkingscenario-e-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [BlinkResultCode](arkts-accessibility-config-blinkresultcode-e-sys.md) |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [9300000](../errorcode-accessibility.md#9300000-无障碍系统服务工作异常) |

**示例**

```TypeScript
import { config } from '@kit.AccessibilityKit';

try {
  let code: config.BlinkResultCode = config.stopBlinking(config.BlinkingMode.SINGLE_BLINK, config.BlinkingScenario.ALARM);
  console.info(`Succeeded in stopBlinking, result code: ${code}`);
} catch (err) {
  console.error(`Failed to call stopBlinking, code is ${err.code}, message is ${err.message}`);
}
```
