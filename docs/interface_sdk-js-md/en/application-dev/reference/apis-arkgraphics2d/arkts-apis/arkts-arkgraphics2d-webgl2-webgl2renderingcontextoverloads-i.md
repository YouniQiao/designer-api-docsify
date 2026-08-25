# WebGL2RenderingContextOverloads

WebGL 2.0

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**System capability:** SystemCapability.Graphic.Graphic2D.WebGL2

## bufferData

```TypeScript
bufferData(target: webgl.GLenum, size: webgl.GLsizeiptr, usage: webgl.GLenum): void
```

Sets buffer data

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.Graphic.Graphic2D.WebGL2

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| target | webgl.GLenum | Yes |
| size | webgl.GLsizeiptr | Yes |
| usage | webgl.GLenum | Yes |

## bufferData

```TypeScript
bufferData(target: webgl.GLenum, srcData: BufferSource | null, usage: webgl.GLenum): void
```

Sets buffer data from BufferSource

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.Graphic.Graphic2D.WebGL2

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| target | webgl.GLenum | Yes |
| srcData | BufferSource \| null | Yes |
| usage | webgl.GLenum | Yes |

## bufferData

```TypeScript
bufferData(
      target: webgl.GLenum,
      srcData: ArrayBufferView,
      usage: webgl.GLenum,
      srcOffset: webgl.GLuint,
      length?: webgl.GLuint,
    ): void
```

Sets buffer data from ArrayBufferView with offset

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.Graphic.Graphic2D.WebGL2

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| target | webgl.GLenum | Yes |
| srcData | [ArrayBufferView](../../apis-arkts/arkts-apis/arkts-arkts-arraybuffer-arraybufferview-i.md) | Yes |
| usage | webgl.GLenum | Yes |
| srcOffset | webgl.GLuint | Yes |
| length | webgl.GLuint | No |

## bufferSubData

```TypeScript
bufferSubData(target: webgl.GLenum, dstByteOffset: webgl.GLintptr, srcData: BufferSource): void
```

Sets buffer sub data

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.Graphic.Graphic2D.WebGL2

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| target | webgl.GLenum | Yes |
| dstByteOffset | webgl.GLintptr | Yes |
| srcData | BufferSource | Yes |

## bufferSubData

```TypeScript
bufferSubData(
      target: webgl.GLenum,
      dstByteOffset: webgl.GLintptr,
      srcData: ArrayBufferView,
      srcOffset: webgl.GLuint,
      length?: webgl.GLuint,
    ): void
```

Sets buffer sub data with offset

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.Graphic.Graphic2D.WebGL2

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| target | webgl.GLenum | Yes |
| dstByteOffset | webgl.GLintptr | Yes |
| srcData | [ArrayBufferView](../../apis-arkts/arkts-apis/arkts-arkts-arraybuffer-arraybufferview-i.md) | Yes |
| srcOffset | webgl.GLuint | Yes |
| length | webgl.GLuint | No |

## compressedTexImage2D

```TypeScript
compressedTexImage2D(
      target: webgl.GLenum,
      level: webgl.GLint,
      internalformat: webgl.GLenum,
      width: webgl.GLsizei,
      height: webgl.GLsizei,
      border: webgl.GLint,
      imageSize: webgl.GLsizei,
      offset: webgl.GLintptr,
    ): void
```

Compressed texture image 2D from PBO offset

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.Graphic.Graphic2D.WebGL2

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| target | webgl.GLenum | Yes |
| level | webgl.GLint | Yes |
| internalformat | webgl.GLenum | Yes |
| width | webgl.GLsizei | Yes |
| height | webgl.GLsizei | Yes |
| border | webgl.GLint | Yes |
| imageSize | webgl.GLsizei | Yes |
| offset | webgl.GLintptr | Yes |

## compressedTexImage2D

```TypeScript
compressedTexImage2D(
      target: webgl.GLenum,
      level: webgl.GLint,
      internalformat: webgl.GLenum,
      width: webgl.GLsizei,
      height: webgl.GLsizei,
      border: webgl.GLint,
      srcData: ArrayBufferView,
      srcOffset?: webgl.GLuint,
      srcLengthOverride?: webgl.GLuint,
    ): void
```

Compressed texture image 2D from ArrayBufferView

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.Graphic.Graphic2D.WebGL2

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| target | webgl.GLenum | Yes |
| level | webgl.GLint | Yes |
| internalformat | webgl.GLenum | Yes |
| width | webgl.GLsizei | Yes |
| height | webgl.GLsizei | Yes |
| border | webgl.GLint | Yes |
| srcData | [ArrayBufferView](../../apis-arkts/arkts-apis/arkts-arkts-arraybuffer-arraybufferview-i.md) | Yes |
| srcOffset | webgl.GLuint | No |
| srcLengthOverride | webgl.GLuint | No |

## compressedTexSubImage2D

```TypeScript
compressedTexSubImage2D(
      target: webgl.GLenum,
      level: webgl.GLint,
      xoffset: webgl.GLint,
      yoffset: webgl.GLint,
      width: webgl.GLsizei,
      height: webgl.GLsizei,
      format: webgl.GLenum,
      imageSize: webgl.GLsizei,
      offset: webgl.GLintptr,
    ): void
```

Compressed texture sub image 2D from PBO offset

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.Graphic.Graphic2D.WebGL2

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| target | webgl.GLenum | Yes |
| level | webgl.GLint | Yes |
| xoffset | webgl.GLint | Yes |
| yoffset | webgl.GLint | Yes |
| width | webgl.GLsizei | Yes |
| height | webgl.GLsizei | Yes |
| format | webgl.GLenum | Yes |
| imageSize | webgl.GLsizei | Yes |
| offset | webgl.GLintptr | Yes |

## compressedTexSubImage2D

```TypeScript
compressedTexSubImage2D(
      target: webgl.GLenum,
      level: webgl.GLint,
      xoffset: webgl.GLint,
      yoffset: webgl.GLint,
      width: webgl.GLsizei,
      height: webgl.GLsizei,
      format: webgl.GLenum,
      srcData: ArrayBufferView,
      srcOffset?: webgl.GLuint,
      srcLengthOverride?: webgl.GLuint,
    ): void
```

Compressed texture sub image 2D from ArrayBufferView

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.Graphic.Graphic2D.WebGL2

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| target | webgl.GLenum | Yes |
| level | webgl.GLint | Yes |
| xoffset | webgl.GLint | Yes |
| yoffset | webgl.GLint | Yes |
| width | webgl.GLsizei | Yes |
| height | webgl.GLsizei | Yes |
| format | webgl.GLenum | Yes |
| srcData | [ArrayBufferView](../../apis-arkts/arkts-apis/arkts-arkts-arraybuffer-arraybufferview-i.md) | Yes |
| srcOffset | webgl.GLuint | No |
| srcLengthOverride | webgl.GLuint | No |

## readPixels

```TypeScript
readPixels(
      x: webgl.GLint,
      y: webgl.GLint,
      width: webgl.GLsizei,
      height: webgl.GLsizei,
      format: webgl.GLenum,
      type: webgl.GLenum,
      dstData: ArrayBufferView | null,
    ): void
```

Reads pixels from the framebuffer to ArrayBufferView

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.Graphic.Graphic2D.WebGL2

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | webgl.GLint | Yes |
| y | webgl.GLint | Yes |
| width | webgl.GLsizei | Yes |
| height | webgl.GLsizei | Yes |
| format | webgl.GLenum | Yes |
| type | webgl.GLenum | Yes |
| dstData | ArrayBufferView \| null | Yes |

## readPixels

```TypeScript
readPixels(
      x: webgl.GLint,
      y: webgl.GLint,
      width: webgl.GLsizei,
      height: webgl.GLsizei,
      format: webgl.GLenum,
      type: webgl.GLenum,
      offset: webgl.GLintptr,
    ): void
```

Reads pixels from the framebuffer to PBO offset

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.Graphic.Graphic2D.WebGL2

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | webgl.GLint | Yes |
| y | webgl.GLint | Yes |
| width | webgl.GLsizei | Yes |
| height | webgl.GLsizei | Yes |
| format | webgl.GLenum | Yes |
| type | webgl.GLenum | Yes |
| offset | webgl.GLintptr | Yes |

## readPixels

```TypeScript
readPixels(
      x: webgl.GLint,
      y: webgl.GLint,
      width: webgl.GLsizei,
      height: webgl.GLsizei,
      format: webgl.GLenum,
      type: webgl.GLenum,
      dstData: ArrayBufferView,
      dstOffset: webgl.GLuint,
    ): void
```

Reads pixels from the framebuffer to ArrayBufferView with offset

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.Graphic.Graphic2D.WebGL2

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | webgl.GLint | Yes |
| y | webgl.GLint | Yes |
| width | webgl.GLsizei | Yes |
| height | webgl.GLsizei | Yes |
| format | webgl.GLenum | Yes |
| type | webgl.GLenum | Yes |
| dstData | [ArrayBufferView](../../apis-arkts/arkts-apis/arkts-arkts-arraybuffer-arraybufferview-i.md) | Yes |
| dstOffset | webgl.GLuint | Yes |

## texImage2D

```TypeScript
texImage2D(
      target: webgl.GLenum,
      level: webgl.GLint,
      internalformat: webgl.GLint,
      width: webgl.GLsizei,
      height: webgl.GLsizei,
      border: webgl.GLint,
      format: webgl.GLenum,
      type: webgl.GLenum,
      pixels: ArrayBufferView | null,
    ): void
```

Sets texture image 2D from pixels

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.Graphic.Graphic2D.WebGL2

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| target | webgl.GLenum | Yes |
| level | webgl.GLint | Yes |
| internalformat | webgl.GLint | Yes |
| width | webgl.GLsizei | Yes |
| height | webgl.GLsizei | Yes |
| border | webgl.GLint | Yes |
| format | webgl.GLenum | Yes |
| type | webgl.GLenum | Yes |
| [pixels](../../apis-image-kit/arkts-apis/arkts-image-image-positionarea-i.md) | ArrayBufferView \| null | Yes |

## texImage2D

```TypeScript
texImage2D(
      target: webgl.GLenum,
      level: webgl.GLint,
      internalformat: webgl.GLint,
      format: webgl.GLenum,
      type: webgl.GLenum,
      source: webgl.TexImageSource,
    ): void
```

Sets texture image 2D from TexImageSource

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.Graphic.Graphic2D.WebGL2

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| target | webgl.GLenum | Yes |
| level | webgl.GLint | Yes |
| internalformat | webgl.GLint | Yes |
| format | webgl.GLenum | Yes |
| type | webgl.GLenum | Yes |
| source | webgl.TexImageSource | Yes |

## texImage2D

```TypeScript
texImage2D(
      target: webgl.GLenum,
      level: webgl.GLint,
      internalformat: webgl.GLint,
      width: webgl.GLsizei,
      height: webgl.GLsizei,
      border: webgl.GLint,
      format: webgl.GLenum,
      type: webgl.GLenum,
      pboOffset: webgl.GLintptr,
    ): void
```

Sets texture image 2D from PBO offset

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.Graphic.Graphic2D.WebGL2

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| target | webgl.GLenum | Yes |
| level | webgl.GLint | Yes |
| internalformat | webgl.GLint | Yes |
| width | webgl.GLsizei | Yes |
| height | webgl.GLsizei | Yes |
| border | webgl.GLint | Yes |
| format | webgl.GLenum | Yes |
| type | webgl.GLenum | Yes |
| pboOffset | webgl.GLintptr | Yes |

## texImage2D

```TypeScript
texImage2D(
      target: webgl.GLenum,
      level: webgl.GLint,
      internalformat: webgl.GLint,
      width: webgl.GLsizei,
      height: webgl.GLsizei,
      border: webgl.GLint,
      format: webgl.GLenum,
      type: webgl.GLenum,
      source: webgl.TexImageSource,
    ): void
```

Sets texture image 2D from TexImageSource

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.Graphic.Graphic2D.WebGL2

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| target | webgl.GLenum | Yes |
| level | webgl.GLint | Yes |
| internalformat | webgl.GLint | Yes |
| width | webgl.GLsizei | Yes |
| height | webgl.GLsizei | Yes |
| border | webgl.GLint | Yes |
| format | webgl.GLenum | Yes |
| type | webgl.GLenum | Yes |
| source | webgl.TexImageSource | Yes |

## texImage2D

```TypeScript
texImage2D(
      target: webgl.GLenum,
      level: webgl.GLint,
      internalformat: webgl.GLint,
      width: webgl.GLsizei,
      height: webgl.GLsizei,
      border: webgl.GLint,
      format: webgl.GLenum,
      type: webgl.GLenum,
      srcData: ArrayBufferView,
      srcOffset: webgl.GLuint,
    ): void
```

Sets texture image 2D from ArrayBufferView with offset

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.Graphic.Graphic2D.WebGL2

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| target | webgl.GLenum | Yes |
| level | webgl.GLint | Yes |
| internalformat | webgl.GLint | Yes |
| width | webgl.GLsizei | Yes |
| height | webgl.GLsizei | Yes |
| border | webgl.GLint | Yes |
| format | webgl.GLenum | Yes |
| type | webgl.GLenum | Yes |
| srcData | [ArrayBufferView](../../apis-arkts/arkts-apis/arkts-arkts-arraybuffer-arraybufferview-i.md) | Yes |
| srcOffset | webgl.GLuint | Yes |

## texSubImage2D

```TypeScript
texSubImage2D(
      target: webgl.GLenum,
      level: webgl.GLint,
      xoffset: webgl.GLint,
      yoffset: webgl.GLint,
      width: webgl.GLsizei,
      height: webgl.GLsizei,
      format: webgl.GLenum,
      type: webgl.GLenum,
      pixels: ArrayBufferView | null,
    ): void
```

Sets texture sub image 2D from pixels

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.Graphic.Graphic2D.WebGL2

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| target | webgl.GLenum | Yes |
| level | webgl.GLint | Yes |
| xoffset | webgl.GLint | Yes |
| yoffset | webgl.GLint | Yes |
| width | webgl.GLsizei | Yes |
| height | webgl.GLsizei | Yes |
| format | webgl.GLenum | Yes |
| type | webgl.GLenum | Yes |
| [pixels](../../apis-image-kit/arkts-apis/arkts-image-image-positionarea-i.md) | ArrayBufferView \| null | Yes |

## texSubImage2D

```TypeScript
texSubImage2D(
      target: webgl.GLenum,
      level: webgl.GLint,
      xoffset: webgl.GLint,
      yoffset: webgl.GLint,
      format: webgl.GLenum,
      type: webgl.GLenum,
      source: webgl.TexImageSource,
    ): void
```

Sets texture sub image 2D from TexImageSource

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.Graphic.Graphic2D.WebGL2

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| target | webgl.GLenum | Yes |
| level | webgl.GLint | Yes |
| xoffset | webgl.GLint | Yes |
| yoffset | webgl.GLint | Yes |
| format | webgl.GLenum | Yes |
| type | webgl.GLenum | Yes |
| source | webgl.TexImageSource | Yes |

## texSubImage2D

```TypeScript
texSubImage2D(
      target: webgl.GLenum,
      level: webgl.GLint,
      xoffset: webgl.GLint,
      yoffset: webgl.GLint,
      width: webgl.GLsizei,
      height: webgl.GLsizei,
      format: webgl.GLenum,
      type: webgl.GLenum,
      pboOffset: webgl.GLintptr,
    ): void
```

Sets texture sub image 2D from PBO offset

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.Graphic.Graphic2D.WebGL2

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| target | webgl.GLenum | Yes |
| level | webgl.GLint | Yes |
| xoffset | webgl.GLint | Yes |
| yoffset | webgl.GLint | Yes |
| width | webgl.GLsizei | Yes |
| height | webgl.GLsizei | Yes |
| format | webgl.GLenum | Yes |
| type | webgl.GLenum | Yes |
| pboOffset | webgl.GLintptr | Yes |

## texSubImage2D

```TypeScript
texSubImage2D(
      target: webgl.GLenum,
      level: webgl.GLint,
      xoffset: webgl.GLint,
      yoffset: webgl.GLint,
      width: webgl.GLsizei,
      height: webgl.GLsizei,
      format: webgl.GLenum,
      type: webgl.GLenum,
      source: webgl.TexImageSource,
    ): void
```

Sets texture sub image 2D from TexImageSource

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.Graphic.Graphic2D.WebGL2

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| target | webgl.GLenum | Yes |
| level | webgl.GLint | Yes |
| xoffset | webgl.GLint | Yes |
| yoffset | webgl.GLint | Yes |
| width | webgl.GLsizei | Yes |
| height | webgl.GLsizei | Yes |
| format | webgl.GLenum | Yes |
| type | webgl.GLenum | Yes |
| source | webgl.TexImageSource | Yes |

## texSubImage2D

```TypeScript
texSubImage2D(
      target: webgl.GLenum,
      level: webgl.GLint,
      xoffset: webgl.GLint,
      yoffset: webgl.GLint,
      width: webgl.GLsizei,
      height: webgl.GLsizei,
      format: webgl.GLenum,
      type: webgl.GLenum,
      srcData: ArrayBufferView,
      srcOffset: webgl.GLuint,
    ): void
```

Sets texture sub image 2D from ArrayBufferView with offset

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.Graphic.Graphic2D.WebGL2

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| target | webgl.GLenum | Yes |
| level | webgl.GLint | Yes |
| xoffset | webgl.GLint | Yes |
| yoffset | webgl.GLint | Yes |
| width | webgl.GLsizei | Yes |
| height | webgl.GLsizei | Yes |
| format | webgl.GLenum | Yes |
| type | webgl.GLenum | Yes |
| srcData | [ArrayBufferView](../../apis-arkts/arkts-apis/arkts-arkts-arraybuffer-arraybufferview-i.md) | Yes |
| srcOffset | webgl.GLuint | Yes |

## uniform1fv

```TypeScript
uniform1fv(
      location: webgl.WebGLUniformLocation | null,
      data: webgl.Float32List,
      srcOffset?: webgl.GLuint,
      srcLength?: webgl.GLuint,
    ): void
```

Sets uniform1fv value

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.Graphic.Graphic2D.WebGL2

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| location | webgl.WebGLUniformLocation \| null | Yes |
| data | webgl.Float32List | Yes |
| srcOffset | webgl.GLuint | No |
| srcLength | webgl.GLuint | No |

## uniform1iv

```TypeScript
uniform1iv(
      location: webgl.WebGLUniformLocation | null,
      data: webgl.Int32List,
      srcOffset?: webgl.GLuint,
      srcLength?: webgl.GLuint,
    ): void
```

Sets uniform1iv value

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.Graphic.Graphic2D.WebGL2

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| location | webgl.WebGLUniformLocation \| null | Yes |
| data | webgl.Int32List | Yes |
| srcOffset | webgl.GLuint | No |
| srcLength | webgl.GLuint | No |

## uniform2fv

```TypeScript
uniform2fv(
      location: webgl.WebGLUniformLocation | null,
      data: webgl.Float32List,
      srcOffset?: webgl.GLuint,
      srcLength?: webgl.GLuint,
    ): void
```

Sets uniform2fv value

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.Graphic.Graphic2D.WebGL2

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| location | webgl.WebGLUniformLocation \| null | Yes |
| data | webgl.Float32List | Yes |
| srcOffset | webgl.GLuint | No |
| srcLength | webgl.GLuint | No |

## uniform2iv

```TypeScript
uniform2iv(
      location: webgl.WebGLUniformLocation | null,
      data: webgl.Int32List,
      srcOffset?: webgl.GLuint,
      srcLength?: webgl.GLuint,
    ): void
```

Sets uniform2iv value

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.Graphic.Graphic2D.WebGL2

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| location | webgl.WebGLUniformLocation \| null | Yes |
| data | webgl.Int32List | Yes |
| srcOffset | webgl.GLuint | No |
| srcLength | webgl.GLuint | No |

## uniform3fv

```TypeScript
uniform3fv(
      location: webgl.WebGLUniformLocation | null,
      data: webgl.Float32List,
      srcOffset?: webgl.GLuint,
      srcLength?: webgl.GLuint,
    ): void
```

Sets uniform3fv value

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.Graphic.Graphic2D.WebGL2

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| location | webgl.WebGLUniformLocation \| null | Yes |
| data | webgl.Float32List | Yes |
| srcOffset | webgl.GLuint | No |
| srcLength | webgl.GLuint | No |

## uniform3iv

```TypeScript
uniform3iv(
      location: webgl.WebGLUniformLocation | null,
      data: webgl.Int32List,
      srcOffset?: webgl.GLuint,
      srcLength?: webgl.GLuint,
    ): void
```

Sets uniform3iv value

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.Graphic.Graphic2D.WebGL2

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| location | webgl.WebGLUniformLocation \| null | Yes |
| data | webgl.Int32List | Yes |
| srcOffset | webgl.GLuint | No |
| srcLength | webgl.GLuint | No |

## uniform4fv

```TypeScript
uniform4fv(
      location: webgl.WebGLUniformLocation | null,
      data: webgl.Float32List,
      srcOffset?: webgl.GLuint,
      srcLength?: webgl.GLuint,
    ): void
```

Sets uniform4fv value

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.Graphic.Graphic2D.WebGL2

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| location | webgl.WebGLUniformLocation \| null | Yes |
| data | webgl.Float32List | Yes |
| srcOffset | webgl.GLuint | No |
| srcLength | webgl.GLuint | No |

## uniform4iv

```TypeScript
uniform4iv(
      location: webgl.WebGLUniformLocation | null,
      data: webgl.Int32List,
      srcOffset?: webgl.GLuint,
      srcLength?: webgl.GLuint,
    ): void
```

Sets uniform4iv value

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.Graphic.Graphic2D.WebGL2

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| location | webgl.WebGLUniformLocation \| null | Yes |
| data | webgl.Int32List | Yes |
| srcOffset | webgl.GLuint | No |
| srcLength | webgl.GLuint | No |

## uniformMatrix2fv

```TypeScript
uniformMatrix2fv(
      location: webgl.WebGLUniformLocation | null,
      transpose: webgl.GLboolean,
      data: webgl.Float32List,
      srcOffset?: webgl.GLuint,
      srcLength?: webgl.GLuint,
    ): void
```

Sets uniformMatrix2fv value

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.Graphic.Graphic2D.WebGL2

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| location | webgl.WebGLUniformLocation \| null | Yes |
| transpose | webgl.GLboolean | Yes |
| data | webgl.Float32List | Yes |
| srcOffset | webgl.GLuint | No |
| srcLength | webgl.GLuint | No |

## uniformMatrix3fv

```TypeScript
uniformMatrix3fv(
      location: webgl.WebGLUniformLocation | null,
      transpose: webgl.GLboolean,
      data: webgl.Float32List,
      srcOffset?: webgl.GLuint,
      srcLength?: webgl.GLuint,
    ): void
```

Sets uniformMatrix3fv value

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.Graphic.Graphic2D.WebGL2

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| location | webgl.WebGLUniformLocation \| null | Yes |
| transpose | webgl.GLboolean | Yes |
| data | webgl.Float32List | Yes |
| srcOffset | webgl.GLuint | No |
| srcLength | webgl.GLuint | No |

## uniformMatrix4fv

```TypeScript
uniformMatrix4fv(
      location: webgl.WebGLUniformLocation | null,
      transpose: webgl.GLboolean,
      data: webgl.Float32List,
      srcOffset?: webgl.GLuint,
      srcLength?: webgl.GLuint,
    ): void
```

Sets uniformMatrix4fv value

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.Graphic.Graphic2D.WebGL2

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| location | webgl.WebGLUniformLocation \| null | Yes |
| transpose | webgl.GLboolean | Yes |
| data | webgl.Float32List | Yes |
| srcOffset | webgl.GLuint | No |
| srcLength | webgl.GLuint | No |
