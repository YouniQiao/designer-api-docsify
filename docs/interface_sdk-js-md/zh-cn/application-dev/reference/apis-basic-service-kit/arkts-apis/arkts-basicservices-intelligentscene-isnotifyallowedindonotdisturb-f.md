# isNotifyAllowedInDoNotDisturb

## 导入模块

```TypeScript
import { intelligentScene } from 'kits/@kit.BasicServicesKit';
```

## isNotifyAllowedInDoNotDisturb

```TypeScript
function isNotifyAllowedInDoNotDisturb(): Promise<boolean>
```

Checks whether calling bundle is allow notify(e.g. sound & vibration) when system Do Not Disturb is on.

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**需要权限：** ohos.permission.GET_DONOTDISTURB_STATE

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-intelligentScene-function isNotifyAllowedInDoNotDisturb(): Promise<boolean>--><!--Device-intelligentScene-function isNotifyAllowedInDoNotDisturb(): Promise<boolean>-End-->

**系统能力：** SystemCapability.Applications.IntelligentScene

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;boolean&gt; | Returns whether notify in Do Not Disturb mode is Allowed. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 35200001 | Internal error. |
| 201 | Permission denied. |

## 示例

```TypeScript
import { BusinessError, intelligentScene } from '@kit.BasicServicesKit';

async function isNotifyAllowedInDoNotDisturb(): Promise<boolean> {
  let isNotifyAllowedInDoNotDisturb: boolean = false;
  try {
    isNotifyAllowedInDoNotDisturb = await intelligentScene.isNotifyAllowedInDoNotDisturb();
  } catch (err) {
    console.error(`Failed to get doNotDisturb state, code: ${err.code}, message: ${err.message}`);
  }
  if (isNotifyAllowedInDoNotDisturb) {
    console.info('Allowed to notify in doNotDisturb state');
  } else {
    console.info('Not allowed to notify in doNotDisturb state or doNotDisturb is closed');
  }
  return isNotifyAllowedInDoNotDisturb;
}
```

