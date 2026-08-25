# GetLiveFormStatusCallback（系统接口）

```TypeScript
type GetLiveFormStatusCallback = () => Record<string, string>
```

Get live form status info callback

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**示例**

ArkTS-Dyn示例：

```TypeScript
import { formInfo } from '@kit.FormKit';

let GetLiveFormStatusCallback: formInfo.GetLiveFormStatusCallback = (): Record<string, string> => {
  return { '1256444': 'ACTIVE' };
};
```

ArkTS-Sta示例：

```TypeScript
'use static'

import { formInfo } from '@kit.FormKit';

let GetLiveFormStatusCallback: formInfo.GetLiveFormStatusCallback = (): Record<string, string> => {
  return { '1256444': 'ACTIVE' };
};
```
