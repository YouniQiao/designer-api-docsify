# addForm（系统接口）

## 导入模块

```TypeScript
import { formHost } from '@kit.FormKit';
```

## addForm

```TypeScript
function addForm(want: Want): Promise<formInfo.RunningFormInfo>
```

Add a form.You can use this method to create a theme form.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.REQUIRE_FORM

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;formInfo.RunningFormInfo & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16500050](../errorcode-form.md#16500050-进程间通信失败) |
| [16500060](../errorcode-form.md#16500060-连接服务失败) |
| [16501000](../errorcode-form.md#16501000-内部功能错误) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { formHost, formInfo } from '@kit.FormKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let want: Want = {
    'bundleName': 'com.huawei.hmsapp.thememanager',
    'abilityName': 'ThemeFaCardUIExtAbility',
    'parameters': {
      'ohos.extra.param.key.form_dimension': 4,
      'ohos.extra.param.key.form_is_theme': true,
      'ohos.extra.param.key.form_location': 0,
      'ohos.extra.param.key.module_name': 'entry',
      'ohos.extra.param.key.form_name': 'widget',
      'themeFormId': '0',
      'themeId': '2181824853'
    }
  };
  formHost.addForm(want).then((data: formInfo.RunningFormInfo) => {
    console.info(`formHost addForm, formId: ${data.formId}`);
  }).catch((error: BusinessError) => {
    console.error(`formHost addForm error, code: ${error.code}, message: ${error.message}`);
  });
} catch (error) {
  console.error(`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}`);
}
```

ArkTS-Sta示例：

```TypeScript
'use static'
import { formInfo, formHost } from '@kit.FormKit';
import { BusinessError, RecordData } from '@kit.BasicServicesKit';
import { Want } from '@kit.AbilityKit';

try {
  let wantParams: Record<String, RecordData> = {
    'ohos.extra.param.key.form_dimension': 4,
    'ohos.extra.param.key.form_is_theme': true,
    'ohos.extra.param.key.form_location': 0,
    'ohos.extra.param.key.module_name': 'entry',
    'ohos.extra.param.key.form_name': 'widget',
    'themeFormId': '0',
    'themeId': '2181824853'
  };
  let want: Want = {
    'bundleName': 'com.huawei.hmsapp.thememanager',
    'abilityName': 'ThemeFaCardUIExtAbility',
    'parameters': wantParams
  }
  formHost.addForm(want).then((data: formInfo.RunningFormInfo) => {
    console.info(`formHost addForm, formId: ${data.formId}`);
  }).catch((error) => {
    console.error(`formHost addForm error, code: ${error.code}, message: ${error.message}`);
  });
} catch (error) {
  console.error(`catch error, ${error.code}, message: ${error.message}`);
}
```
