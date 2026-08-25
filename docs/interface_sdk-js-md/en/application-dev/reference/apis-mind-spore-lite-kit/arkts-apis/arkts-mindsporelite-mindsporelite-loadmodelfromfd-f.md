# loadModelFromFd

## Modules to Import

```TypeScript
import { mindSporeLite } from 'kits/@kit.MindSporeLiteKit';
```

## loadModelFromFd

```TypeScript
function loadModelFromFd(
    model: number,
    context?: Context): Promise<Model>
```

Creates a Model instance file description

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.AI.MindSporeLite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| model | number | Yes |
| context | [Context](arkts-mindsporelite-mindsporelite-context-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Model](arkts-mindsporelite-mindsporelite-model-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| 1000001 |
| 1000007 |


## loadModelFromFd

```TypeScript
function loadModelFromFd(
    model: number, callback: Callback<Model>): void
```

Create a Model instance from file description

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.AI.MindSporeLite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| model | number | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[Model](arkts-mindsporelite-mindsporelite-model-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 1000001 |
| 1000007 |


## loadModelFromFd

```TypeScript
function loadModelFromFd(
    model: number,
    context: Context, callback: Callback<Model>): void
```

Create a Model instance from file description

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.AI.MindSporeLite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| model | number | Yes |
| context | [Context](arkts-mindsporelite-mindsporelite-context-i.md) | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[Model](arkts-mindsporelite-mindsporelite-model-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 1000001 |
| 1000007 |
