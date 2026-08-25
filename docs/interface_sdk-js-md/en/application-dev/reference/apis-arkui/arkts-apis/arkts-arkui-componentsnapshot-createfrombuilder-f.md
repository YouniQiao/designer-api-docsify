# createFromBuilder

## Modules to Import

```TypeScript
import { componentSnapshot } from 'kits/@kit.ArkUI';
```

## createFromBuilder

```TypeScript
function createFromBuilder(builder: CustomBuilder, callback: AsyncCallback<image.PixelMap>,
    delay?: number, checkImageStatus?: boolean, options?: SnapshotOptions): void
```

Renders a custom component in the application background and outputs its snapshot. This API uses an asynchronous callback to return the result. The coordinates and size of the offscreen component's drawing area can be obtained through the callback.

> **NOTE：**&gt;
> - Since API version 12, you can use the [getComponentSnapshot](arkts-arkui-arkui-uicontext-uicontext-c.md#getcomponentsnapshot)
> API in [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) to obtain the [ComponentSnapshot](arkts-arkui-arkui-uicontext-componentsnapshot-c.md)
> object associated with the current UI context.&gt;
> - To account for the time spent in awaiting component building and rendering, the callback of offscreen snapshots
> has a delay of less than 500 ms.&gt;
> - Components in the builder do not support the setting of animation-related attributes, such as
> transition.&gt;
> - If a component is on a time-consuming task, for example, an Image or Web component
> that is loading online images, its loading may be still in progress when this API is called. In this case, the
> output snapshot does not represent the component in the way it looks when the loading is successfully completed.

**Since:** 10

**Deprecated since:** 18

**Substitutes:** createFromBuilder

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| builder | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;image.PixelMap&gt; | Yes |
| delay | number | No |
| checkImageStatus | boolean | No |
| options | [SnapshotOptions](arkts-arkui-componentsnapshot-snapshotoptions-i.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [100001](../errorcode-internal.md#100001-internal-error) |
| [160001](../errorcode-snapshot.md#160001-image-loading-error) |


## createFromBuilder

```TypeScript
function createFromBuilder(builder: CustomBuilder, delay?: number,
    checkImageStatus?: boolean, options?: SnapshotOptions): Promise<image.PixelMap>
```

Renders a custom component in the application background and outputs its snapshot. This API uses a promise to return the result. The coordinates and size of the offscreen component's drawing area can be obtained through the callback.

> **NOTE：**&gt;
> - Since API version 12, you can use the [getComponentSnapshot](arkts-arkui-arkui-uicontext-uicontext-c.md#getcomponentsnapshot)
> API in [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) to obtain the [ComponentSnapshot](arkts-arkui-arkui-uicontext-componentsnapshot-c.md)
> object associated with the current UI context.&gt;
> - To account for the time spent in awaiting component building and rendering, the callback of offscreen snapshots
> has a delay of less than 500 ms.&gt;
> - Components in the builder do not support the setting of animation-related attributes, such as
> transition.&gt;
> - If a component is on a time-consuming task, for example, an Image or Web component
> that is loading online images, its loading may be still in progress when this API is called. In this case, the
> output snapshot does not represent the component in the way it looks when the loading is successfully completed.

**Since:** 10

**Deprecated since:** 18

**Substitutes:** createFromBuilder

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| builder | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | Yes |
| delay | number | No |
| checkImageStatus | boolean | No |
| options | [SnapshotOptions](arkts-arkui-componentsnapshot-snapshotoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;image.PixelMap & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [100001](../errorcode-internal.md#100001-internal-error) |
| [160001](../errorcode-snapshot.md#160001-image-loading-error) |
