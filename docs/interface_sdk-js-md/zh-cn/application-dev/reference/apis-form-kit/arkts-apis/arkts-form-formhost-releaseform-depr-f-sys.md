# releaseForm（系统接口）

## 导入模块

```TypeScript
```

## releaseForm

```TypeScript
function releaseForm(formId: string, callback: AsyncCallback<void>): void
```

释放指定的卡片。调用此方法后，应用程序将无法使用该卡片，但卡片管理器服务仍然保留有关该卡片的缓存信息和存储信息。使用callback异步回调。

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为8。

**废弃版本：** 9

**替代接口：** [releaseForm](arkts-form-formhost-releaseform-f-sys.md)

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
formHost.releaseForm(formId, (error: Base.BusinessError) => {
  if (error.code) {
    console.error(`formHost releaseForm, error: ${JSON.stringify(error)}`);
  } else {
    console.info('formHost releaseForm success');
  }
});
```

```TypeScript
import Base from '@ohos.base';

let formId: string = '12400633174999288';
formHost.releaseForm(formId, true, (error: Base.BusinessError) => {
  if (error.code) {
    console.error(`formHost releaseForm, error: ${JSON.stringify(error)}`);
  } else {
    console.info('formHost releaseForm success');
  }
});
```

```TypeScript
import Base from '@ohos.base';

let formId: string = '12400633174999288';
formHost.releaseForm(formId, true).then(() => {
  console.info('formHost releaseForm success');
}).catch((error: Base.BusinessError) => {
  console.error(`formHost releaseForm, error: ${JSON.stringify(error)}`);
});
```


## releaseForm

```TypeScript
function releaseForm(formId: string, isReleaseCache: boolean, callback: AsyncCallback<void>): void
```

释放指定的卡片。调用此方法后，应用程序将无法使用该卡片，卡片管理器服务保留有关该卡片的存储信息，可以选择是否保留缓存信息。使用callback异步回调。

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为8。

**废弃版本：** 9

**替代接口：** [releaseForm](arkts-form-formhost-releaseform-f-sys.md)

**需要权限：** ohos.permission.REQUIRE_FORM

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| formId | string | 是 |
| isReleaseCache | boolean | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**示例**

参见 [releaseForm](#releaseform)


## releaseForm

```TypeScript
function releaseForm(formId: string, isReleaseCache?: boolean): Promise<void>
```

释放指定的卡片。调用此方法后，应用程序将无法使用该卡片，卡片管理器服务保留有关该卡片的存储信息，可以选择是否保留缓存信息。使用Promise异步回调。

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为8。

**废弃版本：** 9

**替代接口：** [releaseForm](arkts-form-formhost-releaseform-f-sys.md)

**需要权限：** ohos.permission.REQUIRE_FORM

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| formId | string | 是 |
| isReleaseCache | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**示例**

参见 [releaseForm](#releaseform)
