# WebGLRenderingContextOverloads

WebGL 1.0

**Since:** 7

**Deprecated since:** -1

<!--Device-unnamed-interface WebGLRenderingContextOverloads--><!--Device-unnamed-interface WebGLRenderingContextOverloads-End-->

**System capability:** SystemCapability.Graphic.Graphic2D.WebGL

## bufferData

```TypeScript
bufferData(target: GLenum, size: GLsizeiptr, usage: GLenum): void
```

Sets buffer data

**Since:** 7

**Deprecated since:** -1

**Model restriction:** This API can be used only in the FA model.

<!--Device-WebGLRenderingContextOverloads-bufferData(target: GLenum, size: GLsizeiptr, usage: GLenum): void--><!--Device-WebGLRenderingContextOverloads-bufferData(target: GLenum, size: GLsizeiptr, usage: GLenum): void-End-->

**System capability:** SystemCapability.Graphic.Graphic2D.WebGL

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| target | [GLenum](arkts-arkgraphics2d-glenum-t.md) | Yes |
| size | [GLsizeiptr](arkts-arkgraphics2d-glsizeiptr-t.md) | Yes |
| usage | [GLenum](arkts-arkgraphics2d-glenum-t.md) | Yes |

## bufferData

```TypeScript
bufferData(target: GLenum, data: BufferSource | null, usage: GLenum): void
```

Sets buffer data from BufferSource

**Since:** 7

**Deprecated since:** -1

**Model restriction:** This API can be used only in the FA model.

<!--Device-WebGLRenderingContextOverloads-bufferData(target: GLenum, data: BufferSource | null, usage: GLenum): void--><!--Device-WebGLRenderingContextOverloads-bufferData(target: GLenum, data: BufferSource | null, usage: GLenum): void-End-->

**System capability:** SystemCapability.Graphic.Graphic2D.WebGL

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| target | [GLenum](arkts-arkgraphics2d-glenum-t.md) | Yes |
| data | BufferSource \| null | Yes |
| usage | [GLenum](arkts-arkgraphics2d-glenum-t.md) | Yes |

## bufferSubData

```TypeScript
bufferSubData(target: GLenum, offset: GLintptr, data: BufferSource): void
```

Sets buffer sub data

**Since:** 7

**Deprecated since:** -1

**Model restriction:** This API can be used only in the FA model.

<!--Device-WebGLRenderingContextOverloads-bufferSubData(target: GLenum, offset: GLintptr, data: BufferSource): void--><!--Device-WebGLRenderingContextOverloads-bufferSubData(target: GLenum, offset: GLintptr, data: BufferSource): void-End-->

**System capability:** SystemCapability.Graphic.Graphic2D.WebGL

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| target | [GLenum](arkts-arkgraphics2d-glenum-t.md) | Yes |
| offset | [GLintptr](arkts-arkgraphics2d-glintptr-t.md) | Yes |
| data | BufferSource | Yes |

## compressedTexImage2D

```TypeScript
compressedTexImage2D(
      target: GLenum,
      level: GLint,
      internalformat: GLenum,
      width: GLsizei,
      height: GLsizei,
      border: GLint,
      data: ArrayBufferView,
    ): void
```

Compressed texture image 2D

**Since:** 7

**Deprecated since:** -1

**Model restriction:** This API can be used only in the FA model.

<!--Device-WebGLRenderingContextOverloads-compressedTexImage2D(      target: GLenum,      level: GLint,      internalformat: GLenum,      width: GLsizei,      height: GLsizei,      border: GLint,      data: ArrayBufferView,    ): void--><!--Device-WebGLRenderingContextOverloads-compressedTexImage2D(      target: GLenum,      level: GLint,      internalformat: GLenum,      width: GLsizei,      height: GLsizei,      border: GLint,      data: ArrayBufferView,    ): void-End-->

**System capability:** SystemCapability.Graphic.Graphic2D.WebGL

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| target | [GLenum](arkts-arkgraphics2d-glenum-t.md) | Yes |
| level | [GLint](arkts-arkgraphics2d-glint-t.md) | Yes |
| internalformat | [GLenum](arkts-arkgraphics2d-glenum-t.md) | Yes |
| width | [GLsizei](arkts-arkgraphics2d-glsizei-t.md) | Yes |
| height | [GLsizei](arkts-arkgraphics2d-glsizei-t.md) | Yes |
| border | [GLint](arkts-arkgraphics2d-glint-t.md) | Yes |
| data | [ArrayBufferView](../../apis-na/arkts-apis/arkts-na-lib-es5-arraybufferview-i.md) | Yes |

## compressedTexSubImage2D

```TypeScript
compressedTexSubImage2D(
      target: GLenum,
      level: GLint,
      xoffset: GLint,
      yoffset: GLint,
      width: GLsizei,
      height: GLsizei,
      format: GLenum,
      data: ArrayBufferView,
    ): void
```

Compressed texture sub image 2D

**Since:** 7

**Deprecated since:** -1

**Model restriction:** This API can be used only in the FA model.

<!--Device-WebGLRenderingContextOverloads-compressedTexSubImage2D(      target: GLenum,      level: GLint,      xoffset: GLint,      yoffset: GLint,      width: GLsizei,      height: GLsizei,      format: GLenum,      data: ArrayBufferView,    ): void--><!--Device-WebGLRenderingContextOverloads-compressedTexSubImage2D(      target: GLenum,      level: GLint,      xoffset: GLint,      yoffset: GLint,      width: GLsizei,      height: GLsizei,      format: GLenum,      data: ArrayBufferView,    ): void-End-->

**System capability:** SystemCapability.Graphic.Graphic2D.WebGL

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| target | [GLenum](arkts-arkgraphics2d-glenum-t.md) | Yes |
| level | [GLint](arkts-arkgraphics2d-glint-t.md) | Yes |
| xoffset | [GLint](arkts-arkgraphics2d-glint-t.md) | Yes |
| yoffset | [GLint](arkts-arkgraphics2d-glint-t.md) | Yes |
| width | [GLsizei](arkts-arkgraphics2d-glsizei-t.md) | Yes |
| height | [GLsizei](arkts-arkgraphics2d-glsizei-t.md) | Yes |
| format | [GLenum](arkts-arkgraphics2d-glenum-t.md) | Yes |
| data | [ArrayBufferView](../../apis-na/arkts-apis/arkts-na-lib-es5-arraybufferview-i.md) | Yes |

## readPixels

```TypeScript
readPixels(
      x: GLint,
      y: GLint,
      width: GLsizei,
      height: GLsizei,
      format: GLenum,
      type: GLenum,
      pixels: ArrayBufferView | null,
    ): void
```

Reads pixels from the framebuffer

**Since:** 7

**Deprecated since:** -1

**Model restriction:** This API can be used only in the FA model.

<!--Device-WebGLRenderingContextOverloads-readPixels(      x: GLint,      y: GLint,      width: GLsizei,      height: GLsizei,      format: GLenum,      type: GLenum,      pixels: ArrayBufferView | null,    ): void--><!--Device-WebGLRenderingContextOverloads-readPixels(      x: GLint,      y: GLint,      width: GLsizei,      height: GLsizei,      format: GLenum,      type: GLenum,      pixels: ArrayBufferView | null,    ): void-End-->

**System capability:** SystemCapability.Graphic.Graphic2D.WebGL

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | [GLint](arkts-arkgraphics2d-glint-t.md) | Yes |
| y | [GLint](arkts-arkgraphics2d-glint-t.md) | Yes |
| width | [GLsizei](arkts-arkgraphics2d-glsizei-t.md) | Yes |
| height | [GLsizei](arkts-arkgraphics2d-glsizei-t.md) | Yes |
| format | [GLenum](arkts-arkgraphics2d-glenum-t.md) | Yes |
| type | [GLenum](arkts-arkgraphics2d-glenum-t.md) | Yes |
| [pixels](../../apis-image-kit/arkts-apis/arkts-image-image-positionarea-i.md) | [ArrayBufferView](../../apis-na/arkts-apis/arkts-na-lib-es5-arraybufferview-i.md) \| null | Yes |

## texImage2D

```TypeScript
texImage2D(
      target: GLenum,
      level: GLint,
      internalformat: GLint,
      width: GLsizei,
      height: GLsizei,
      border: GLint,
      format: GLenum,
      type: GLenum,
      pixels: ArrayBufferView | null,
    ): void
```

Sets texture image 2D from pixels

**Since:** 7

**Deprecated since:** -1

**Model restriction:** This API can be used only in the FA model.

<!--Device-WebGLRenderingContextOverloads-texImage2D(      target: GLenum,      level: GLint,      internalformat: GLint,      width: GLsizei,      height: GLsizei,      border: GLint,      format: GLenum,      type: GLenum,      pixels: ArrayBufferView | null,    ): void--><!--Device-WebGLRenderingContextOverloads-texImage2D(      target: GLenum,      level: GLint,      internalformat: GLint,      width: GLsizei,      height: GLsizei,      border: GLint,      format: GLenum,      type: GLenum,      pixels: ArrayBufferView | null,    ): void-End-->

**System capability:** SystemCapability.Graphic.Graphic2D.WebGL

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| target | [GLenum](arkts-arkgraphics2d-glenum-t.md) | Yes |
| level | [GLint](arkts-arkgraphics2d-glint-t.md) | Yes |
| internalformat | [GLint](arkts-arkgraphics2d-glint-t.md) | Yes |
| width | [GLsizei](arkts-arkgraphics2d-glsizei-t.md) | Yes |
| height | [GLsizei](arkts-arkgraphics2d-glsizei-t.md) | Yes |
| border | [GLint](arkts-arkgraphics2d-glint-t.md) | Yes |
| format | [GLenum](arkts-arkgraphics2d-glenum-t.md) | Yes |
| type | [GLenum](arkts-arkgraphics2d-glenum-t.md) | Yes |
| [pixels](../../apis-image-kit/arkts-apis/arkts-image-image-positionarea-i.md) | [ArrayBufferView](../../apis-na/arkts-apis/arkts-na-lib-es5-arraybufferview-i.md) \| null | Yes |

## texImage2D

```TypeScript
texImage2D(
      target: GLenum,
      level: GLint,
      internalformat: GLint,
      format: GLenum,
      type: GLenum,
      source: TexImageSource,
    ): void
```

Sets texture image 2D from TexImageSource

**Since:** 7

**Deprecated since:** -1

**Model restriction:** This API can be used only in the FA model.

<!--Device-WebGLRenderingContextOverloads-texImage2D(      target: GLenum,      level: GLint,      internalformat: GLint,      format: GLenum,      type: GLenum,      source: TexImageSource,    ): void--><!--Device-WebGLRenderingContextOverloads-texImage2D(      target: GLenum,      level: GLint,      internalformat: GLint,      format: GLenum,      type: GLenum,      source: TexImageSource,    ): void-End-->

**System capability:** SystemCapability.Graphic.Graphic2D.WebGL

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| target | [GLenum](arkts-arkgraphics2d-glenum-t.md) | Yes |
| level | [GLint](arkts-arkgraphics2d-glint-t.md) | Yes |
| internalformat | [GLint](arkts-arkgraphics2d-glint-t.md) | Yes |
| format | [GLenum](arkts-arkgraphics2d-glenum-t.md) | Yes |
| type | [GLenum](arkts-arkgraphics2d-glenum-t.md) | Yes |
| source | [TexImageSource](arkts-arkgraphics2d-teximagesource-t.md) | Yes |

## texSubImage2D

```TypeScript
texSubImage2D(
      target: GLenum,
      level: GLint,
      xoffset: GLint,
      yoffset: GLint,
      width: GLsizei,
      height: GLsizei,
      format: GLenum,
      type: GLenum,
      pixels: ArrayBufferView | null,
    ): void
```

Sets texture sub image 2D from pixels

**Since:** 7

**Deprecated since:** -1

**Model restriction:** This API can be used only in the FA model.

<!--Device-WebGLRenderingContextOverloads-texSubImage2D(      target: GLenum,      level: GLint,      xoffset: GLint,      yoffset: GLint,      width: GLsizei,      height: GLsizei,      format: GLenum,      type: GLenum,      pixels: ArrayBufferView | null,    ): void--><!--Device-WebGLRenderingContextOverloads-texSubImage2D(      target: GLenum,      level: GLint,      xoffset: GLint,      yoffset: GLint,      width: GLsizei,      height: GLsizei,      format: GLenum,      type: GLenum,      pixels: ArrayBufferView | null,    ): void-End-->

**System capability:** SystemCapability.Graphic.Graphic2D.WebGL

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| target | [GLenum](arkts-arkgraphics2d-glenum-t.md) | Yes |
| level | [GLint](arkts-arkgraphics2d-glint-t.md) | Yes |
| xoffset | [GLint](arkts-arkgraphics2d-glint-t.md) | Yes |
| yoffset | [GLint](arkts-arkgraphics2d-glint-t.md) | Yes |
| width | [GLsizei](arkts-arkgraphics2d-glsizei-t.md) | Yes |
| height | [GLsizei](arkts-arkgraphics2d-glsizei-t.md) | Yes |
| format | [GLenum](arkts-arkgraphics2d-glenum-t.md) | Yes |
| type | [GLenum](arkts-arkgraphics2d-glenum-t.md) | Yes |
| [pixels](../../apis-image-kit/arkts-apis/arkts-image-image-positionarea-i.md) | [ArrayBufferView](../../apis-na/arkts-apis/arkts-na-lib-es5-arraybufferview-i.md) \| null | Yes |

## texSubImage2D

```TypeScript
texSubImage2D(
      target: GLenum,
      level: GLint,
      xoffset: GLint,
      yoffset: GLint,
      format: GLenum,
      type: GLenum,
      source: TexImageSource,
    ): void
```

Sets texture sub image 2D from TexImageSource

**Since:** 7

**Deprecated since:** -1

**Model restriction:** This API can be used only in the FA model.

<!--Device-WebGLRenderingContextOverloads-texSubImage2D(      target: GLenum,      level: GLint,      xoffset: GLint,      yoffset: GLint,      format: GLenum,      type: GLenum,      source: TexImageSource,    ): void--><!--Device-WebGLRenderingContextOverloads-texSubImage2D(      target: GLenum,      level: GLint,      xoffset: GLint,      yoffset: GLint,      format: GLenum,      type: GLenum,      source: TexImageSource,    ): void-End-->

**System capability:** SystemCapability.Graphic.Graphic2D.WebGL

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| target | [GLenum](arkts-arkgraphics2d-glenum-t.md) | Yes |
| level | [GLint](arkts-arkgraphics2d-glint-t.md) | Yes |
| xoffset | [GLint](arkts-arkgraphics2d-glint-t.md) | Yes |
| yoffset | [GLint](arkts-arkgraphics2d-glint-t.md) | Yes |
| format | [GLenum](arkts-arkgraphics2d-glenum-t.md) | Yes |
| type | [GLenum](arkts-arkgraphics2d-glenum-t.md) | Yes |
| source | [TexImageSource](arkts-arkgraphics2d-teximagesource-t.md) | Yes |

## uniform1fv

```TypeScript
uniform1fv(location: WebGLUniformLocation | null, v: Float32List): void
```

Sets uniform1fv value

**Since:** 7

**Deprecated since:** -1

**Model restriction:** This API can be used only in the FA model.

<!--Device-WebGLRenderingContextOverloads-uniform1fv(location: WebGLUniformLocation | null, v: Float32List): void--><!--Device-WebGLRenderingContextOverloads-uniform1fv(location: WebGLUniformLocation | null, v: Float32List): void-End-->

**System capability:** SystemCapability.Graphic.Graphic2D.WebGL

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| location | [WebGLUniformLocation](arkts-arkgraphics2d-webgl-webgluniformlocation-i.md) \| null | Yes |
| v | [Float32List](arkts-arkgraphics2d-float32list-t.md) | Yes |

## uniform1iv

```TypeScript
uniform1iv(location: WebGLUniformLocation | null, v: Int32List): void
```

Sets uniform1iv value

**Since:** 7

**Deprecated since:** -1

**Model restriction:** This API can be used only in the FA model.

<!--Device-WebGLRenderingContextOverloads-uniform1iv(location: WebGLUniformLocation | null, v: Int32List): void--><!--Device-WebGLRenderingContextOverloads-uniform1iv(location: WebGLUniformLocation | null, v: Int32List): void-End-->

**System capability:** SystemCapability.Graphic.Graphic2D.WebGL

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| location | [WebGLUniformLocation](arkts-arkgraphics2d-webgl-webgluniformlocation-i.md) \| null | Yes |
| v | [Int32List](arkts-arkgraphics2d-int32list-t.md) | Yes |

## uniform2fv

```TypeScript
uniform2fv(location: WebGLUniformLocation | null, v: Float32List): void
```

Sets uniform2fv value

**Since:** 7

**Deprecated since:** -1

**Model restriction:** This API can be used only in the FA model.

<!--Device-WebGLRenderingContextOverloads-uniform2fv(location: WebGLUniformLocation | null, v: Float32List): void--><!--Device-WebGLRenderingContextOverloads-uniform2fv(location: WebGLUniformLocation | null, v: Float32List): void-End-->

**System capability:** SystemCapability.Graphic.Graphic2D.WebGL

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| location | [WebGLUniformLocation](arkts-arkgraphics2d-webgl-webgluniformlocation-i.md) \| null | Yes |
| v | [Float32List](arkts-arkgraphics2d-float32list-t.md) | Yes |

## uniform2iv

```TypeScript
uniform2iv(location: WebGLUniformLocation | null, v: Int32List): void
```

Sets uniform2iv value

**Since:** 7

**Deprecated since:** -1

**Model restriction:** This API can be used only in the FA model.

<!--Device-WebGLRenderingContextOverloads-uniform2iv(location: WebGLUniformLocation | null, v: Int32List): void--><!--Device-WebGLRenderingContextOverloads-uniform2iv(location: WebGLUniformLocation | null, v: Int32List): void-End-->

**System capability:** SystemCapability.Graphic.Graphic2D.WebGL

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| location | [WebGLUniformLocation](arkts-arkgraphics2d-webgl-webgluniformlocation-i.md) \| null | Yes |
| v | [Int32List](arkts-arkgraphics2d-int32list-t.md) | Yes |

## uniform3fv

```TypeScript
uniform3fv(location: WebGLUniformLocation | null, v: Float32List): void
```

Sets uniform3fv value

**Since:** 7

**Deprecated since:** -1

**Model restriction:** This API can be used only in the FA model.

<!--Device-WebGLRenderingContextOverloads-uniform3fv(location: WebGLUniformLocation | null, v: Float32List): void--><!--Device-WebGLRenderingContextOverloads-uniform3fv(location: WebGLUniformLocation | null, v: Float32List): void-End-->

**System capability:** SystemCapability.Graphic.Graphic2D.WebGL

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| location | [WebGLUniformLocation](arkts-arkgraphics2d-webgl-webgluniformlocation-i.md) \| null | Yes |
| v | [Float32List](arkts-arkgraphics2d-float32list-t.md) | Yes |

## uniform3iv

```TypeScript
uniform3iv(location: WebGLUniformLocation | null, v: Int32List): void
```

Sets uniform3iv value

**Since:** 7

**Deprecated since:** -1

**Model restriction:** This API can be used only in the FA model.

<!--Device-WebGLRenderingContextOverloads-uniform3iv(location: WebGLUniformLocation | null, v: Int32List): void--><!--Device-WebGLRenderingContextOverloads-uniform3iv(location: WebGLUniformLocation | null, v: Int32List): void-End-->

**System capability:** SystemCapability.Graphic.Graphic2D.WebGL

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| location | [WebGLUniformLocation](arkts-arkgraphics2d-webgl-webgluniformlocation-i.md) \| null | Yes |
| v | [Int32List](arkts-arkgraphics2d-int32list-t.md) | Yes |

## uniform4fv

```TypeScript
uniform4fv(location: WebGLUniformLocation | null, v: Float32List): void
```

Sets uniform4fv value

**Since:** 7

**Deprecated since:** -1

**Model restriction:** This API can be used only in the FA model.

<!--Device-WebGLRenderingContextOverloads-uniform4fv(location: WebGLUniformLocation | null, v: Float32List): void--><!--Device-WebGLRenderingContextOverloads-uniform4fv(location: WebGLUniformLocation | null, v: Float32List): void-End-->

**System capability:** SystemCapability.Graphic.Graphic2D.WebGL

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| location | [WebGLUniformLocation](arkts-arkgraphics2d-webgl-webgluniformlocation-i.md) \| null | Yes |
| v | [Float32List](arkts-arkgraphics2d-float32list-t.md) | Yes |

## uniform4iv

```TypeScript
uniform4iv(location: WebGLUniformLocation | null, v: Int32List): void
```

Sets uniform4iv value

**Since:** 7

**Deprecated since:** -1

**Model restriction:** This API can be used only in the FA model.

<!--Device-WebGLRenderingContextOverloads-uniform4iv(location: WebGLUniformLocation | null, v: Int32List): void--><!--Device-WebGLRenderingContextOverloads-uniform4iv(location: WebGLUniformLocation | null, v: Int32List): void-End-->

**System capability:** SystemCapability.Graphic.Graphic2D.WebGL

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| location | [WebGLUniformLocation](arkts-arkgraphics2d-webgl-webgluniformlocation-i.md) \| null | Yes |
| v | [Int32List](arkts-arkgraphics2d-int32list-t.md) | Yes |

## uniformMatrix2fv

```TypeScript
uniformMatrix2fv(location: WebGLUniformLocation | null, transpose: GLboolean, value: Float32List): void
```

Sets uniformMatrix2fv value

**Since:** 7

**Deprecated since:** -1

**Model restriction:** This API can be used only in the FA model.

<!--Device-WebGLRenderingContextOverloads-uniformMatrix2fv(location: WebGLUniformLocation | null, transpose: GLboolean, value: Float32List): void--><!--Device-WebGLRenderingContextOverloads-uniformMatrix2fv(location: WebGLUniformLocation | null, transpose: GLboolean, value: Float32List): void-End-->

**System capability:** SystemCapability.Graphic.Graphic2D.WebGL

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| location | [WebGLUniformLocation](arkts-arkgraphics2d-webgl-webgluniformlocation-i.md) \| null | Yes |
| transpose | [GLboolean](arkts-arkgraphics2d-glboolean-t.md) | Yes |
| value | [Float32List](arkts-arkgraphics2d-float32list-t.md) | Yes |

## uniformMatrix3fv

```TypeScript
uniformMatrix3fv(location: WebGLUniformLocation | null, transpose: GLboolean, value: Float32List): void
```

Sets uniformMatrix3fv value

**Since:** 7

**Deprecated since:** -1

**Model restriction:** This API can be used only in the FA model.

<!--Device-WebGLRenderingContextOverloads-uniformMatrix3fv(location: WebGLUniformLocation | null, transpose: GLboolean, value: Float32List): void--><!--Device-WebGLRenderingContextOverloads-uniformMatrix3fv(location: WebGLUniformLocation | null, transpose: GLboolean, value: Float32List): void-End-->

**System capability:** SystemCapability.Graphic.Graphic2D.WebGL

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| location | [WebGLUniformLocation](arkts-arkgraphics2d-webgl-webgluniformlocation-i.md) \| null | Yes |
| transpose | [GLboolean](arkts-arkgraphics2d-glboolean-t.md) | Yes |
| value | [Float32List](arkts-arkgraphics2d-float32list-t.md) | Yes |

## uniformMatrix4fv

```TypeScript
uniformMatrix4fv(location: WebGLUniformLocation | null, transpose: GLboolean, value: Float32List): void
```

Sets uniformMatrix4fv value

**Since:** 7

**Deprecated since:** -1

**Model restriction:** This API can be used only in the FA model.

<!--Device-WebGLRenderingContextOverloads-uniformMatrix4fv(location: WebGLUniformLocation | null, transpose: GLboolean, value: Float32List): void--><!--Device-WebGLRenderingContextOverloads-uniformMatrix4fv(location: WebGLUniformLocation | null, transpose: GLboolean, value: Float32List): void-End-->

**System capability:** SystemCapability.Graphic.Graphic2D.WebGL

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| location | [WebGLUniformLocation](arkts-arkgraphics2d-webgl-webgluniformlocation-i.md) \| null | Yes |
| transpose | [GLboolean](arkts-arkgraphics2d-glboolean-t.md) | Yes |
| value | [Float32List](arkts-arkgraphics2d-float32list-t.md) | Yes |
