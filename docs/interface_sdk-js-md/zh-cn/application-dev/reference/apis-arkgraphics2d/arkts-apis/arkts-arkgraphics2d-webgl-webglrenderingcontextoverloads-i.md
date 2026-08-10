# WebGLRenderingContextOverloads

WebGL 1.0

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

<!--Device-unnamed-interface WebGLRenderingContextOverloads--><!--Device-unnamed-interface WebGLRenderingContextOverloads-End-->

**系统能力：** SystemCapability.Graphic.Graphic2D.WebGL

## bufferData

```TypeScript
bufferData(target: GLenum, size: GLsizeiptr, usage: GLenum): void
```

Sets buffer data

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-WebGLRenderingContextOverloads-bufferData(target: GLenum, size: GLsizeiptr, usage: GLenum): void--><!--Device-WebGLRenderingContextOverloads-bufferData(target: GLenum, size: GLsizeiptr, usage: GLenum): void-End-->

**系统能力：** SystemCapability.Graphic.Graphic2D.WebGL

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| target | [GLenum](arkts-arkgraphics2d-glenum-t.md) | 是 | Buffer target |
| size | [GLsizeiptr](arkts-arkgraphics2d-glsizeiptr-t.md) | 是 | Buffer size |
| usage | [GLenum](arkts-arkgraphics2d-glenum-t.md) | 是 | Buffer usage |

## bufferData

```TypeScript
bufferData(target: GLenum, data: BufferSource | null, usage: GLenum): void
```

Sets buffer data from BufferSource

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-WebGLRenderingContextOverloads-bufferData(target: GLenum, data: BufferSource | null, usage: GLenum): void--><!--Device-WebGLRenderingContextOverloads-bufferData(target: GLenum, data: BufferSource | null, usage: GLenum): void-End-->

**系统能力：** SystemCapability.Graphic.Graphic2D.WebGL

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| target | [GLenum](arkts-arkgraphics2d-glenum-t.md) | 是 | Buffer target |
| data | BufferSource \| null | 是 | Buffer data |
| usage | [GLenum](arkts-arkgraphics2d-glenum-t.md) | 是 | Buffer usage |

## bufferSubData

```TypeScript
bufferSubData(target: GLenum, offset: GLintptr, data: BufferSource): void
```

Sets buffer sub data

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-WebGLRenderingContextOverloads-bufferSubData(target: GLenum, offset: GLintptr, data: BufferSource): void--><!--Device-WebGLRenderingContextOverloads-bufferSubData(target: GLenum, offset: GLintptr, data: BufferSource): void-End-->

**系统能力：** SystemCapability.Graphic.Graphic2D.WebGL

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| target | [GLenum](arkts-arkgraphics2d-glenum-t.md) | 是 | Buffer target |
| offset | [GLintptr](arkts-arkgraphics2d-glintptr-t.md) | 是 | Offset |
| data | BufferSource | 是 | Data to set |

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

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-WebGLRenderingContextOverloads-compressedTexImage2D(      target: GLenum,      level: GLint,      internalformat: GLenum,      width: GLsizei,      height: GLsizei,      border: GLint,      data: ArrayBufferView,    ): void--><!--Device-WebGLRenderingContextOverloads-compressedTexImage2D(      target: GLenum,      level: GLint,      internalformat: GLenum,      width: GLsizei,      height: GLsizei,      border: GLint,      data: ArrayBufferView,    ): void-End-->

**系统能力：** SystemCapability.Graphic.Graphic2D.WebGL

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| target | [GLenum](arkts-arkgraphics2d-glenum-t.md) | 是 | Texture target |
| level | [GLint](arkts-arkgraphics2d-glint-t.md) | 是 | Mipmap level |
| internalformat | [GLenum](arkts-arkgraphics2d-glenum-t.md) | 是 | Internal format |
| width | [GLsizei](arkts-arkgraphics2d-glsizei-t.md) | 是 | Width |
| height | [GLsizei](arkts-arkgraphics2d-glsizei-t.md) | 是 | Height |
| border | [GLint](arkts-arkgraphics2d-glint-t.md) | 是 | Border |
| data | [ArrayBufferView](../../apis-arkts/arkts-apis/arkts-arkts-arraybuffer-arraybufferview-i.md) | 是 | Compressed image data |

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

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-WebGLRenderingContextOverloads-compressedTexSubImage2D(      target: GLenum,      level: GLint,      xoffset: GLint,      yoffset: GLint,      width: GLsizei,      height: GLsizei,      format: GLenum,      data: ArrayBufferView,    ): void--><!--Device-WebGLRenderingContextOverloads-compressedTexSubImage2D(      target: GLenum,      level: GLint,      xoffset: GLint,      yoffset: GLint,      width: GLsizei,      height: GLsizei,      format: GLenum,      data: ArrayBufferView,    ): void-End-->

**系统能力：** SystemCapability.Graphic.Graphic2D.WebGL

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| target | [GLenum](arkts-arkgraphics2d-glenum-t.md) | 是 | Texture target |
| level | [GLint](arkts-arkgraphics2d-glint-t.md) | 是 | Mipmap level |
| xoffset | [GLint](arkts-arkgraphics2d-glint-t.md) | 是 | X offset |
| yoffset | [GLint](arkts-arkgraphics2d-glint-t.md) | 是 | Y offset |
| width | [GLsizei](arkts-arkgraphics2d-glsizei-t.md) | 是 | Width |
| height | [GLsizei](arkts-arkgraphics2d-glsizei-t.md) | 是 | Height |
| format | [GLenum](arkts-arkgraphics2d-glenum-t.md) | 是 | Format |
| data | [ArrayBufferView](../../apis-arkts/arkts-apis/arkts-arkts-arraybuffer-arraybufferview-i.md) | 是 | Compressed image data |

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

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-WebGLRenderingContextOverloads-readPixels(      x: GLint,      y: GLint,      width: GLsizei,      height: GLsizei,      format: GLenum,      type: GLenum,      pixels: ArrayBufferView | null,    ): void--><!--Device-WebGLRenderingContextOverloads-readPixels(      x: GLint,      y: GLint,      width: GLsizei,      height: GLsizei,      format: GLenum,      type: GLenum,      pixels: ArrayBufferView | null,    ): void-End-->

**系统能力：** SystemCapability.Graphic.Graphic2D.WebGL

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | [GLint](arkts-arkgraphics2d-glint-t.md) | 是 | X coordinate |
| y | [GLint](arkts-arkgraphics2d-glint-t.md) | 是 | Y coordinate |
| width | [GLsizei](arkts-arkgraphics2d-glsizei-t.md) | 是 | Width |
| height | [GLsizei](arkts-arkgraphics2d-glsizei-t.md) | 是 | Height |
| format | [GLenum](arkts-arkgraphics2d-glenum-t.md) | 是 | Pixel format |
| type | [GLenum](arkts-arkgraphics2d-glenum-t.md) | 是 | Pixel type |
| pixels | [ArrayBufferView](../../apis-arkts/arkts-apis/arkts-arkts-arraybuffer-arraybufferview-i.md) \| null | 是 | Pixel buffer |

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

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-WebGLRenderingContextOverloads-texImage2D(      target: GLenum,      level: GLint,      internalformat: GLint,      width: GLsizei,      height: GLsizei,      border: GLint,      format: GLenum,      type: GLenum,      pixels: ArrayBufferView | null,    ): void--><!--Device-WebGLRenderingContextOverloads-texImage2D(      target: GLenum,      level: GLint,      internalformat: GLint,      width: GLsizei,      height: GLsizei,      border: GLint,      format: GLenum,      type: GLenum,      pixels: ArrayBufferView | null,    ): void-End-->

**系统能力：** SystemCapability.Graphic.Graphic2D.WebGL

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| target | [GLenum](arkts-arkgraphics2d-glenum-t.md) | 是 | Texture target |
| level | [GLint](arkts-arkgraphics2d-glint-t.md) | 是 | Mipmap level |
| internalformat | [GLint](arkts-arkgraphics2d-glint-t.md) | 是 | Internal format |
| width | [GLsizei](arkts-arkgraphics2d-glsizei-t.md) | 是 | Width |
| height | [GLsizei](arkts-arkgraphics2d-glsizei-t.md) | 是 | Height |
| border | [GLint](arkts-arkgraphics2d-glint-t.md) | 是 | Border |
| format | [GLenum](arkts-arkgraphics2d-glenum-t.md) | 是 | Pixel format |
| type | [GLenum](arkts-arkgraphics2d-glenum-t.md) | 是 | Pixel type |
| pixels | [ArrayBufferView](../../apis-arkts/arkts-apis/arkts-arkts-arraybuffer-arraybufferview-i.md) \| null | 是 | Pixel data |

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

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-WebGLRenderingContextOverloads-texImage2D(      target: GLenum,      level: GLint,      internalformat: GLint,      format: GLenum,      type: GLenum,      source: TexImageSource,    ): void--><!--Device-WebGLRenderingContextOverloads-texImage2D(      target: GLenum,      level: GLint,      internalformat: GLint,      format: GLenum,      type: GLenum,      source: TexImageSource,    ): void-End-->

**系统能力：** SystemCapability.Graphic.Graphic2D.WebGL

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| target | [GLenum](arkts-arkgraphics2d-glenum-t.md) | 是 | Texture target |
| level | [GLint](arkts-arkgraphics2d-glint-t.md) | 是 | Mipmap level |
| internalformat | [GLint](arkts-arkgraphics2d-glint-t.md) | 是 | Internal format |
| format | [GLenum](arkts-arkgraphics2d-glenum-t.md) | 是 | Pixel format |
| type | [GLenum](arkts-arkgraphics2d-glenum-t.md) | 是 | Pixel type |
| source | [TexImageSource](arkts-arkgraphics2d-teximagesource-t.md) | 是 | Image source |

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

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-WebGLRenderingContextOverloads-texSubImage2D(      target: GLenum,      level: GLint,      xoffset: GLint,      yoffset: GLint,      width: GLsizei,      height: GLsizei,      format: GLenum,      type: GLenum,      pixels: ArrayBufferView | null,    ): void--><!--Device-WebGLRenderingContextOverloads-texSubImage2D(      target: GLenum,      level: GLint,      xoffset: GLint,      yoffset: GLint,      width: GLsizei,      height: GLsizei,      format: GLenum,      type: GLenum,      pixels: ArrayBufferView | null,    ): void-End-->

**系统能力：** SystemCapability.Graphic.Graphic2D.WebGL

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| target | [GLenum](arkts-arkgraphics2d-glenum-t.md) | 是 | Texture target |
| level | [GLint](arkts-arkgraphics2d-glint-t.md) | 是 | Mipmap level |
| xoffset | [GLint](arkts-arkgraphics2d-glint-t.md) | 是 | X offset |
| yoffset | [GLint](arkts-arkgraphics2d-glint-t.md) | 是 | Y offset |
| width | [GLsizei](arkts-arkgraphics2d-glsizei-t.md) | 是 | Width |
| height | [GLsizei](arkts-arkgraphics2d-glsizei-t.md) | 是 | Height |
| format | [GLenum](arkts-arkgraphics2d-glenum-t.md) | 是 | Pixel format |
| type | [GLenum](arkts-arkgraphics2d-glenum-t.md) | 是 | Pixel type |
| pixels | [ArrayBufferView](../../apis-arkts/arkts-apis/arkts-arkts-arraybuffer-arraybufferview-i.md) \| null | 是 | Pixel data |

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

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-WebGLRenderingContextOverloads-texSubImage2D(      target: GLenum,      level: GLint,      xoffset: GLint,      yoffset: GLint,      format: GLenum,      type: GLenum,      source: TexImageSource,    ): void--><!--Device-WebGLRenderingContextOverloads-texSubImage2D(      target: GLenum,      level: GLint,      xoffset: GLint,      yoffset: GLint,      format: GLenum,      type: GLenum,      source: TexImageSource,    ): void-End-->

**系统能力：** SystemCapability.Graphic.Graphic2D.WebGL

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| target | [GLenum](arkts-arkgraphics2d-glenum-t.md) | 是 | Texture target |
| level | [GLint](arkts-arkgraphics2d-glint-t.md) | 是 | Mipmap level |
| xoffset | [GLint](arkts-arkgraphics2d-glint-t.md) | 是 | X offset |
| yoffset | [GLint](arkts-arkgraphics2d-glint-t.md) | 是 | Y offset |
| format | [GLenum](arkts-arkgraphics2d-glenum-t.md) | 是 | Pixel format |
| type | [GLenum](arkts-arkgraphics2d-glenum-t.md) | 是 | Pixel type |
| source | [TexImageSource](arkts-arkgraphics2d-teximagesource-t.md) | 是 | Image source |

## uniform1fv

```TypeScript
uniform1fv(location: WebGLUniformLocation | null, v: Float32List): void
```

Sets uniform1fv value

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-WebGLRenderingContextOverloads-uniform1fv(location: WebGLUniformLocation | null, v: Float32List): void--><!--Device-WebGLRenderingContextOverloads-uniform1fv(location: WebGLUniformLocation | null, v: Float32List): void-End-->

**系统能力：** SystemCapability.Graphic.Graphic2D.WebGL

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| location | [WebGLUniformLocation](arkts-arkgraphics2d-webgl-webgluniformlocation-i.md) \| null | 是 | Uniform location |
| v | [Float32List](arkts-arkgraphics2d-float32list-t.md) | 是 | Value array |

## uniform1iv

```TypeScript
uniform1iv(location: WebGLUniformLocation | null, v: Int32List): void
```

Sets uniform1iv value

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-WebGLRenderingContextOverloads-uniform1iv(location: WebGLUniformLocation | null, v: Int32List): void--><!--Device-WebGLRenderingContextOverloads-uniform1iv(location: WebGLUniformLocation | null, v: Int32List): void-End-->

**系统能力：** SystemCapability.Graphic.Graphic2D.WebGL

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| location | [WebGLUniformLocation](arkts-arkgraphics2d-webgl-webgluniformlocation-i.md) \| null | 是 | Uniform location |
| v | [Int32List](arkts-arkgraphics2d-int32list-t.md) | 是 | Value array |

## uniform2fv

```TypeScript
uniform2fv(location: WebGLUniformLocation | null, v: Float32List): void
```

Sets uniform2fv value

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-WebGLRenderingContextOverloads-uniform2fv(location: WebGLUniformLocation | null, v: Float32List): void--><!--Device-WebGLRenderingContextOverloads-uniform2fv(location: WebGLUniformLocation | null, v: Float32List): void-End-->

**系统能力：** SystemCapability.Graphic.Graphic2D.WebGL

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| location | [WebGLUniformLocation](arkts-arkgraphics2d-webgl-webgluniformlocation-i.md) \| null | 是 | Uniform location |
| v | [Float32List](arkts-arkgraphics2d-float32list-t.md) | 是 | Value array |

## uniform2iv

```TypeScript
uniform2iv(location: WebGLUniformLocation | null, v: Int32List): void
```

Sets uniform2iv value

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-WebGLRenderingContextOverloads-uniform2iv(location: WebGLUniformLocation | null, v: Int32List): void--><!--Device-WebGLRenderingContextOverloads-uniform2iv(location: WebGLUniformLocation | null, v: Int32List): void-End-->

**系统能力：** SystemCapability.Graphic.Graphic2D.WebGL

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| location | [WebGLUniformLocation](arkts-arkgraphics2d-webgl-webgluniformlocation-i.md) \| null | 是 | Uniform location |
| v | [Int32List](arkts-arkgraphics2d-int32list-t.md) | 是 | Value array |

## uniform3fv

```TypeScript
uniform3fv(location: WebGLUniformLocation | null, v: Float32List): void
```

Sets uniform3fv value

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-WebGLRenderingContextOverloads-uniform3fv(location: WebGLUniformLocation | null, v: Float32List): void--><!--Device-WebGLRenderingContextOverloads-uniform3fv(location: WebGLUniformLocation | null, v: Float32List): void-End-->

**系统能力：** SystemCapability.Graphic.Graphic2D.WebGL

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| location | [WebGLUniformLocation](arkts-arkgraphics2d-webgl-webgluniformlocation-i.md) \| null | 是 | Uniform location |
| v | [Float32List](arkts-arkgraphics2d-float32list-t.md) | 是 | Value array |

## uniform3iv

```TypeScript
uniform3iv(location: WebGLUniformLocation | null, v: Int32List): void
```

Sets uniform3iv value

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-WebGLRenderingContextOverloads-uniform3iv(location: WebGLUniformLocation | null, v: Int32List): void--><!--Device-WebGLRenderingContextOverloads-uniform3iv(location: WebGLUniformLocation | null, v: Int32List): void-End-->

**系统能力：** SystemCapability.Graphic.Graphic2D.WebGL

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| location | [WebGLUniformLocation](arkts-arkgraphics2d-webgl-webgluniformlocation-i.md) \| null | 是 | Uniform location |
| v | [Int32List](arkts-arkgraphics2d-int32list-t.md) | 是 | Value array |

## uniform4fv

```TypeScript
uniform4fv(location: WebGLUniformLocation | null, v: Float32List): void
```

Sets uniform4fv value

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-WebGLRenderingContextOverloads-uniform4fv(location: WebGLUniformLocation | null, v: Float32List): void--><!--Device-WebGLRenderingContextOverloads-uniform4fv(location: WebGLUniformLocation | null, v: Float32List): void-End-->

**系统能力：** SystemCapability.Graphic.Graphic2D.WebGL

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| location | [WebGLUniformLocation](arkts-arkgraphics2d-webgl-webgluniformlocation-i.md) \| null | 是 | Uniform location |
| v | [Float32List](arkts-arkgraphics2d-float32list-t.md) | 是 | Value array |

## uniform4iv

```TypeScript
uniform4iv(location: WebGLUniformLocation | null, v: Int32List): void
```

Sets uniform4iv value

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-WebGLRenderingContextOverloads-uniform4iv(location: WebGLUniformLocation | null, v: Int32List): void--><!--Device-WebGLRenderingContextOverloads-uniform4iv(location: WebGLUniformLocation | null, v: Int32List): void-End-->

**系统能力：** SystemCapability.Graphic.Graphic2D.WebGL

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| location | [WebGLUniformLocation](arkts-arkgraphics2d-webgl-webgluniformlocation-i.md) \| null | 是 | Uniform location |
| v | [Int32List](arkts-arkgraphics2d-int32list-t.md) | 是 | Value array |

## uniformMatrix2fv

```TypeScript
uniformMatrix2fv(location: WebGLUniformLocation | null, transpose: GLboolean, value: Float32List): void
```

Sets uniformMatrix2fv value

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-WebGLRenderingContextOverloads-uniformMatrix2fv(location: WebGLUniformLocation | null, transpose: GLboolean, value: Float32List): void--><!--Device-WebGLRenderingContextOverloads-uniformMatrix2fv(location: WebGLUniformLocation | null, transpose: GLboolean, value: Float32List): void-End-->

**系统能力：** SystemCapability.Graphic.Graphic2D.WebGL

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| location | [WebGLUniformLocation](arkts-arkgraphics2d-webgl-webgluniformlocation-i.md) \| null | 是 | Uniform location |
| transpose | [GLboolean](arkts-arkgraphics2d-glboolean-t.md) | 是 | Whether to transpose |
| value | [Float32List](arkts-arkgraphics2d-float32list-t.md) | 是 | Matrix value |

## uniformMatrix3fv

```TypeScript
uniformMatrix3fv(location: WebGLUniformLocation | null, transpose: GLboolean, value: Float32List): void
```

Sets uniformMatrix3fv value

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-WebGLRenderingContextOverloads-uniformMatrix3fv(location: WebGLUniformLocation | null, transpose: GLboolean, value: Float32List): void--><!--Device-WebGLRenderingContextOverloads-uniformMatrix3fv(location: WebGLUniformLocation | null, transpose: GLboolean, value: Float32List): void-End-->

**系统能力：** SystemCapability.Graphic.Graphic2D.WebGL

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| location | [WebGLUniformLocation](arkts-arkgraphics2d-webgl-webgluniformlocation-i.md) \| null | 是 | Uniform location |
| transpose | [GLboolean](arkts-arkgraphics2d-glboolean-t.md) | 是 | Whether to transpose |
| value | [Float32List](arkts-arkgraphics2d-float32list-t.md) | 是 | Matrix value |

## uniformMatrix4fv

```TypeScript
uniformMatrix4fv(location: WebGLUniformLocation | null, transpose: GLboolean, value: Float32List): void
```

Sets uniformMatrix4fv value

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-WebGLRenderingContextOverloads-uniformMatrix4fv(location: WebGLUniformLocation | null, transpose: GLboolean, value: Float32List): void--><!--Device-WebGLRenderingContextOverloads-uniformMatrix4fv(location: WebGLUniformLocation | null, transpose: GLboolean, value: Float32List): void-End-->

**系统能力：** SystemCapability.Graphic.Graphic2D.WebGL

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| location | [WebGLUniformLocation](arkts-arkgraphics2d-webgl-webgluniformlocation-i.md) \| null | 是 | Uniform location |
| transpose | [GLboolean](arkts-arkgraphics2d-glboolean-t.md) | 是 | Whether to transpose |
| value | [Float32List](arkts-arkgraphics2d-float32list-t.md) | 是 | Matrix value |

