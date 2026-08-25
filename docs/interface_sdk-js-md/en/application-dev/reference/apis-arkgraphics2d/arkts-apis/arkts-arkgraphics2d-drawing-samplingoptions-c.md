# SamplingOptions

Implements sampling options.

> **NOTE：**&gt;
> - The initial APIs of this class are supported since API version 12.&gt;
> - This module uses the physical pixel unit, px.&gt;
> - This module operates under a single-threaded model. The caller needs to manage thread safety and context state
> transitions.

**Since:** 12

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
import { drawing } from 'kits/@kit.ArkGraphics2D';
```

## constructor

```TypeScript
constructor()
```

Creates a **SamplingOptions** object, where the default value of [FilterMode](arkts-arkgraphics2d-drawing-filtermode-e.md) is **FILTER_MODE_NEAREST**.

**Since:** 12

**System capability:** SystemCapability.Graphics.Drawing

## constructor

```TypeScript
constructor(filterMode: FilterMode)
```

Creates a **SamplingOptions** object.

**Since:** 12

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| filterMode | [FilterMode](arkts-arkgraphics2d-drawing-filtermode-e.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
