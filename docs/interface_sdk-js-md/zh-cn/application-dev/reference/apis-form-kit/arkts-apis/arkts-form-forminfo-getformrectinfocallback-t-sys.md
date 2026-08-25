# GetFormRectInfoCallback（系统接口）

```TypeScript
type GetFormRectInfoCallback = (formId: string) => Promise<formInfo.Rect>
```

卡片位置、尺寸查询回调。使用Promise异步回调。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| formId | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[formInfo.Rect](arkts-form-forminfo-rect-i.md)&gt; |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { formInfo } from '@kit.FormKit';

// 卡片使用方需要对查询请求进行处理，计算并返回卡片尺寸、位置信息
let getFormRectInfoCallback: formInfo.GetFormRectInfoCallback =
  (formId: string): Promise<formInfo.Rect> => {
    return new Promise<formInfo.Rect>((resolve: (value: formInfo.Rect) => void) => {
      console.info(`formId is ${formId}`);
      let formRect: formInfo.Rect = {
        left: 0,
        top: 0,
        width: 0,
        height: 0
      };
      resolve(formRect);
    })
  };
```

ArkTS-Sta示例：

```TypeScript
'use static'

import { formInfo } from '@kit.FormKit';

// 卡片使用方需要对查询请求进行处理，计算并返回卡片尺寸、位置信息
let getFormRectInfoCallback: formInfo.GetFormRectInfoCallback =
  (formId: string): Promise<formInfo.Rect> => {
    return new Promise<formInfo.Rect>((
      resolve: (rect: formInfo.Rect) => void, reject: (err: Error) => void): void => {
      let formRect: formInfo.Rect = {
        left: 1.0,
        top: 1.0,
        width: 1.0,
        height: 1.0
      }
      resolve(formRect);
    });
  }
```
