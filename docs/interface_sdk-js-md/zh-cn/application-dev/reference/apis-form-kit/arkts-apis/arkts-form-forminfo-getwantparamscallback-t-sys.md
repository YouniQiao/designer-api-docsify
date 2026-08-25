# GetWantParamsCallback（系统接口）

```TypeScript
type GetWantParamsCallback = (formInfo: Array<formInfo.FormInfo>) => Array<Record<string, Object>>
```

获取卡片参数回调。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [formInfo](arkts-app-form-forminfo.md) | Array&lt;[formInfo.FormInfo](arkts-form-forminfo-forminfo-i.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Array & lt;Record & lt;string, Object & gt; & gt; |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { formInfo } from '@kit.FormKit';

let getWantParamsCallback: formInfo.GetWantParamsCallback =
  (formInfo: Array<formInfo.FormInfo>): Array<Record<string, Object>> => {
    console.info('get want params callback, form count: ' + formInfo.length);
    let wantParamsList: Array<Record<string, Object>> = [];
    for (let i = 0; i < formInfo.length; i++) {
      let params: Record<string, Object> = {
        'key': 'value'
      };
      wantParamsList.push(params);
    }
    return wantParamsList;
  };
```

ArkTS-Sta示例：

```TypeScript
'use static'
import { formInfo } from '@kit.FormKit';

let getWantParamsCallback: formInfo.GetWantParamsCallback =
  (formInfo: Array<formInfo.FormInfo>): Array<Record<string, Object>> => {
    console.info('get want params callback, form count: ' + formInfo.length);
    let wantParamsList: Array<Record<string, Object>> = [];
    for (let i = 0; i < formInfo.length; i++) {
      let params: Record<string, Object> = {
        'key': 'value'
      };
      wantParamsList.push(params);
    }
    return wantParamsList;
  };
```
