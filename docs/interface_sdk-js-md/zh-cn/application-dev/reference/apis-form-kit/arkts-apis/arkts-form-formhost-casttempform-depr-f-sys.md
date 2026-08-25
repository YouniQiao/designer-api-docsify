# castTempForm（系统接口）

## 导入模块

```TypeScript
```

## castTempForm

```TypeScript
function castTempForm(formId: string, callback: AsyncCallback<void>): void
```

将指定的临时卡片转换为普通卡片。使用callback异步回调。

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为8。

**废弃版本：** 9

**替代接口：** castTempForm

**需要权限：** ohos.permission.REQUIRE_FORM

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| formId | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**示例**

```TypeScript
import Base from '@ohos.base';

let formId: string = '12400633174999288';
formHost.castTempForm(formId, (error: Base.BusinessError) => {
  if (error.code) {
    console.error(`formHost castTempForm, error: ${JSON.stringify(error)}`);
  }
});
```

```TypeScript
import Base from '@ohos.base';

let formId: string = '12400633174999288';
formHost.castTempForm(formId).then(() => {
  console.info('formHost castTempForm success');
}).catch((error: Base.BusinessError) => {
  console.error(`formHost castTempForm, error: ${JSON.stringify(error)}`);
});
```


## castTempForm

```TypeScript
function castTempForm(formId: string): Promise<void>
```

将指定的临时卡片转换为普通卡片。使用Promise异步回调。

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为8。

**废弃版本：** 9

**替代接口：** castTempForm

**需要权限：** ohos.permission.REQUIRE_FORM

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| formId | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**示例**

参见 [castTempForm](#casttempform)
