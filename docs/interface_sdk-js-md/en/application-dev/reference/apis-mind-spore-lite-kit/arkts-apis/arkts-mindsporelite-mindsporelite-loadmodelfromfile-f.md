# loadModelFromFile

## Modules to Import

```TypeScript
import { mindSporeLite } from 'kits/@kit.MindSporeLiteKit';
```

## loadModelFromFile

```TypeScript
function loadModelFromFile(
    model: string,
    context?: Context): Promise<Model>
```

Create a Model instance from file path

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.AI.MindSporeLite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| model | string | Yes |
| context | [Context](arkts-mindsporelite-mindsporelite-context-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Model](arkts-mindsporelite-mindsporelite-model-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| 1000000 |
| 1000001 |
| 1000002 |
| 1000003 |


## loadModelFromFile

```TypeScript
function loadModelFromFile(
    model: string, callback: Callback<Model>): void
```

Create a Model instance from file path.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.AI.MindSporeLite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| model | string | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[Model](arkts-mindsporelite-mindsporelite-model-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 1000000 |
| 1000001 |
| 1000002 |
| 1000003 |


## loadModelFromFile

```TypeScript
function loadModelFromFile(
    model: string,
    context: Context, callback: Callback<Model>): void
```

Create a Model instance from file path.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.AI.MindSporeLite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| model | string | Yes |
| context | [Context](arkts-mindsporelite-mindsporelite-context-i.md) | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[Model](arkts-mindsporelite-mindsporelite-model-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 1000000 |
| 1000001 |
| 1000002 |
| 1000003 |
