# disableFormsUpdate（系统接口）

## 导入模块

```TypeScript
```

## disableFormsUpdate

```TypeScript
function disableFormsUpdate(formIds: Array<string>, callback: AsyncCallback<void>): void
```

向卡片框架发送通知以使指定的卡片不可以更新。该方法调用成功后，卡片刷新状态设置为去使能，卡片不可以接收来自卡片提供方的更新。使用callback异步回调。

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为8。

**废弃版本：** 9

**替代接口：** [disableFormsUpdate](arkts-form-formhost-disableformsupdate-f-sys.md)

**需要权限：** ohos.permission.REQUIRE_FORM

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| formIds | Array & lt;string & gt; | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**示例**

```TypeScript
import Base from '@ohos.base';

let formIds: string[] = ['12400633174999288'];
formHost.disableFormsUpdate(formIds, (error: Base.BusinessError) => {
  if (error.code) {
    console.error(`formHost disableFormsUpdate, error: ${JSON.stringify(error)}`);
  }
});
```

```TypeScript
import Base from '@ohos.base';

let formIds: string[] = ['12400633174999288'];
formHost.disableFormsUpdate(formIds).then(() => {
  console.info('formHost disableFormsUpdate success');
}).catch((error: Base.BusinessError) => {
  console.error(`formHost disableFormsUpdate, error: ${JSON.stringify(error)}`);
});
```


## disableFormsUpdate

```TypeScript
function disableFormsUpdate(formIds: Array<string>): Promise<void>
```

向卡片框架发送通知以使指定的卡片不可以更新。该方法调用成功后，卡片刷新状态设置为去使能，卡片不可以接收来自卡片提供方的更新。使用Promise异步回调。

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为8。

**废弃版本：** 9

**替代接口：** [disableFormsUpdate](arkts-form-formhost-disableformsupdate-f-sys.md)

**需要权限：** ohos.permission.REQUIRE_FORM

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| formIds | Array & lt;string & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**示例**

参见 [disableFormsUpdate](#disableformsupdate)
