I-Logix-RPY-Archive version 8.5.2 Modeler C++ 1159120
{ IProject 
	- _id = GUID 49ba43cf-c5df-4d8c-a39f-c46ed211b619;
	- _myState = 8192;
	- _properties = { IPropertyContainer 
		- Subjects = { IRPYRawContainer 
			- size = 1;
			- value = 
			{ IPropertySubject 
				- _Name = "Browser";
				- Metaclasses = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ IPropertyMetaclass 
						- _Name = "Settings";
						- Properties = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IProperty 
								- _Name = "ShowPredefinedPackage";
								- _Value = "False";
								- _Type = Bool;
							}
						}
					}
				}
			}
		}
	}
	- _name = "Projeto_ES670";
	- _objectCreation = "515131334201693092445";
	- _umlDependencyID = "2577";
	- _lastID = 18;
	- _UserColors = { IRPYRawContainer 
		- size = 16;
		- value = 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 
	}
	- _defaultSubsystem = { ISubsystemHandle 
		- _m2Class = "ISubsystem";
		- _filename = "_Projeto_Pratico.sbs";
		- _subsystem = "";
		- _class = "";
		- _name = "_Projeto_Pratico";
		- _id = GUID 20246198-4c47-4bfe-9397-a7aa14ffd20f;
	}
	- _component = { IHandle 
		- _m2Class = "IComponent";
		- _filename = "FRDM_KL25Z.cmp";
		- _subsystem = "";
		- _class = "";
		- _name = "FRDM_KL25Z";
		- _id = GUID 97403057-80a5-4323-8421-7b4a31e27ebf;
	}
	- Multiplicities = { IRPYRawContainer 
		- size = 4;
		- value = 
		{ IMultiplicityItem 
			- _name = "1";
			- _count = -1;
		}
		{ IMultiplicityItem 
			- _name = "*";
			- _count = -1;
		}
		{ IMultiplicityItem 
			- _name = "0,1";
			- _count = -1;
		}
		{ IMultiplicityItem 
			- _name = "1..*";
			- _count = -1;
		}
	}
	- Subsystems = { IRPYRawContainer 
		- size = 10;
		- value = 
		{ ISubsystem 
			- fileName = "_Projeto_Pratico";
			- _id = GUID 20246198-4c47-4bfe-9397-a7aa14ffd20f;
		}
		{ ISubsystem 
			- fileName = "_Requisitos";
			- _id = GUID 83b232d5-cbf5-48de-bd01-d866eaf248e9;
		}
		{ ISubsystem 
			- fileName = "Util";
			- _id = GUID f5d6f4c4-ca70-4386-9866-389eed46d9b7;
		}
		{ ISubsystem 
			- fileName = "KL25Z";
			- _id = GUID 9ac6e8be-1171-4050-a109-3666f2506e5d;
		}
		{ ISubsystem 
			- fileName = "LedSwi";
			- _id = GUID 065e8ea8-3104-4865-9f03-c833c5c57170;
		}
		{ ISubsystem 
			- fileName = "Main";
			- _id = GUID a9bfd00a-eefd-40b0-8807-d7abb8ac9870;
		}
		{ ISubsystem 
			- fileName = "Buzzer";
			- _id = GUID f7399950-29d6-4418-ab30-4039fe4c2874;
		}
		{ ISubsystem 
			- fileName = "GPIO";
			- _id = GUID cecafbf0-ffbd-4124-8cae-f06a2917ce91;
		}
		{ ISubsystem 
			- fileName = "PIT";
			- _id = GUID 83818f05-7053-49e7-ae2f-96b665be83da;
		}
		{ ISubsystem 
			- fileName = "SevenSeg";
			- _id = GUID e536725c-fa59-4de6-a2b0-d993b44d2f45;
		}
	}
	- Diagrams = { IRPYRawContainer 
		- size = 3;
		- value = 
		{ IDiagram 
			- _id = GUID b199a12f-d6a2-434c-8c28-e03ad146546a;
			- _myState = 8192;
			- _properties = { IPropertyContainer 
				- Subjects = { IRPYRawContainer 
					- size = 3;
					- value = 
					{ IPropertySubject 
						- _Name = "Format";
						- Metaclasses = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "Comment";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,84,96";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,207";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "225,225,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Requirement";
								- Properties = { IRPYRawContainer 
									- size = 8;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,84,96";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,207";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Font.Size@Child.NameCompartment@Stereotype";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "225,225,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
						}
					}
					{ IPropertySubject 
						- _Name = "General";
						- Metaclasses = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "Graphics";
								- Properties = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IProperty 
										- _Name = "grid_display";
										- _Value = "False";
										- _Type = Bool;
									}
								}
							}
						}
					}
					{ IPropertySubject 
						- _Name = "ObjectModelGe";
						- Metaclasses = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "Requirement";
								- Properties = { IRPYRawContainer 
									- size = 6;
									- value = 
									{ IProperty 
										- _Name = "Compartments";
										- _Value = "";
										- _Type = MultiLine;
									}
									{ IProperty 
										- _Name = "RequirementNotation";
										- _Value = "Note_Style";
										- _Type = Enum;
										- _ExtraTypeInfo = "Note_Style,Box_Style";
									}
									{ IProperty 
										- _Name = "ShowAnnotationContents";
										- _Value = "Description";
										- _Type = Enum;
										- _ExtraTypeInfo = "Name,Specification,Description,Label";
									}
									{ IProperty 
										- _Name = "ShowForm";
										- _Value = "Note";
										- _Type = Enum;
										- _ExtraTypeInfo = "Plain,Note,Pushpin";
									}
									{ IProperty 
										- _Name = "ShowName";
										- _Value = "Relative";
										- _Type = Enum;
										- _ExtraTypeInfo = "Full_path,Relative,Name_only,Label";
									}
									{ IProperty 
										- _Name = "ShowStereotype";
										- _Value = "Label";
										- _Type = Enum;
										- _ExtraTypeInfo = "Label,Bitmap,None";
									}
								}
							}
						}
					}
				}
			}
			- _name = "diag_requisitos";
			- _objectCreation = "515151334201693092245";
			- _umlDependencyID = "3046";
			- _description = { IDescription 
				- _textRTF = "{\\rtf1\\ansi\\ansicpg1252\\deff0\\deflang1046{\\fonttbl{\\f0\\fnil\\fcharset0 Arial;}}
\\viewkind4\\uc1\\pard\\fs20 Diagrama de requisitos de sistema do projeto pr\\'e1tico da ES670 \\par
\\par
}
";
			}
			- _lastModifiedTime = "1.12.2016::18:42:25";
			- _graphicChart = { CGIClassChart 
				- _id = GUID 2fe99eb3-10f9-42d0-adf7-80beaef157a7;
				- m_type = 0;
				- m_pModelObject = { IHandle 
					- _m2Class = "IDiagram";
					- _id = GUID b199a12f-d6a2-434c-8c28-e03ad146546a;
				}
				- m_pParent = ;
				- m_name = { CGIText 
					- m_str = "";
					- m_style = "Arial" 10 0 0 0 1 ;
					- m_color = { IColor 
						- m_fgColor = 0;
						- m_bgColor = 0;
						- m_bgFlag = 0;
					}
					- m_position = 1 0 0  ;
					- m_nIdent = 0;
					- m_bImplicitSetRectPoints = 0;
					- m_nOrientationCtrlPt = 8;
				}
				- m_drawBehavior = 0;
				- m_bIsPreferencesInitialized = 0;
				- elementList = 11;
				{ CGIClass 
					- _id = GUID 21c3de7b-5b1e-4ece-8aeb-2d905c26c54f;
					- m_type = 78;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "_Projeto_Pratico.sbs";
						- _subsystem = "_Projeto_Pratico";
						- _class = "";
						- _name = "TopLevel";
						- _id = GUID 0d5184b0-4db2-4cdb-a85e-27b5b9b2898f;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "TopLevel";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 0;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 0 ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIAnnotation 
					- _id = GUID 32c27ec7-2ced-47c0-bd63-73a9b3f85834;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 173;
					- m_pModelObject = { IHandle 
						- _m2Class = "IComment";
						- _filename = "_Projeto_Pratico.sbs";
						- _subsystem = "_Projeto_Pratico";
						- _class = "";
						- _name = "comment_0";
						- _id = GUID 28f0689a-ecff-4bb0-941d-4a8badc4b580;
					}
					- m_pParent = GUID 21c3de7b-5b1e-4ece-8aeb-2d905c26c54f;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.568266 0 0 0.0879121 27 28.7363 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 0;
				}
				{ CGIAnnotation 
					- _id = GUID fbc087bd-42f5-463a-89cf-87362a3d0d65;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 3;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Requirement";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Font.Italic";
												- _Value = "0";
												- _Type = Int;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Requirement";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "ID,Specification";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 176;
					- m_pModelObject = { IHandle 
						- _m2Class = "IRequirement";
						- _filename = "_Requisitos.sbs";
						- _subsystem = "_Requisitos";
						- _class = "";
						- _name = "Requisito TECLADO";
						- _id = GUID 166aaab7-cf5c-4481-a4d3-665ede382195;
					}
					- m_pParent = GUID 21c3de7b-5b1e-4ece-8aeb-2d905c26c54f;
					- m_name = { CGIText 
						- m_str = "Requisito TECLADO";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.178967 0 0 0.112637 28 139.662 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=28%,72%>
<frame name=IDTextCompartment>
<frame name=SpecificationTextCompartment>";
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 1;
				}
				{ CGIAnnotation 
					- _id = GUID 957a0848-69a8-4ca6-a987-1a9f43b61b6c;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Requirement";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "ID,Specification";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 176;
					- m_pModelObject = { IHandle 
						- _m2Class = "IRequirement";
						- _filename = "_Requisitos.sbs";
						- _subsystem = "_Requisitos";
						- _class = "";
						- _name = "Requisito LED";
						- _id = GUID ac7c8af3-17dd-4d76-b0be-04c3795263c9;
					}
					- m_pParent = GUID 21c3de7b-5b1e-4ece-8aeb-2d905c26c54f;
					- m_name = { CGIText 
						- m_str = "Requisito LED";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.178967 0 0 0.113553 232 138.659 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=41%,59%>
<frame name=IDTextCompartment>
<frame name=SpecificationTextCompartment>";
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 1;
				}
				{ CGIAnnotation 
					- _id = GUID 354dfa17-ff97-48f4-bea6-90701b76db18;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 3;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Requirement";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Font.Size";
												- _Value = "10";
												- _Type = Int;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Requirement";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "ID,Specification";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 176;
					- m_pModelObject = { IHandle 
						- _m2Class = "IRequirement";
						- _filename = "_Requisitos.sbs";
						- _subsystem = "_Requisitos";
						- _class = "";
						- _name = "Requisito PROTOCOLO";
						- _id = GUID f955129c-5a6e-4c50-b3c4-a546def9576e;
					}
					- m_pParent = GUID 21c3de7b-5b1e-4ece-8aeb-2d905c26c54f;
					- m_name = { CGIText 
						- m_str = "Requisito PROTOCOLO";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.178967 0 0 0.152652 28 274.846 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=25%,75%>
<frame name=IDTextCompartment>
<frame name=SpecificationTextCompartment>";
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 1;
				}
				{ CGIAnnotation 
					- _id = GUID aa2a6d3c-135e-4ecd-9ab5-8bd8722e9a10;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Requirement";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "ID,Specification";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 176;
					- m_pModelObject = { IHandle 
						- _m2Class = "IRequirement";
						- _filename = "_Requisitos.sbs";
						- _subsystem = "_Requisitos";
						- _class = "";
						- _name = "Requisito VELOCIDADE";
						- _id = GUID 0b53c1e4-b7fc-476c-8788-696ee3c1a74c;
					}
					- m_pParent = GUID 21c3de7b-5b1e-4ece-8aeb-2d905c26c54f;
					- m_name = { CGIText 
						- m_str = "Requisito VELOCIDADE";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.178967 0 0 0.119048 437 277.643 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=35%,65%>
<frame name=IDTextCompartment>
<frame name=SpecificationTextCompartment>";
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 1;
				}
				{ CGIAnnotation 
					- _id = GUID 84fca68f-31da-4052-baef-97ffeea9c672;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Requirement";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "ID,Specification";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 176;
					- m_pModelObject = { IHandle 
						- _m2Class = "IRequirement";
						- _filename = "_Requisitos.sbs";
						- _subsystem = "_Requisitos";
						- _class = "";
						- _name = "Requisito PWM";
						- _id = GUID eaa58628-4ade-4046-9928-56f257060a65;
					}
					- m_pParent = GUID 21c3de7b-5b1e-4ece-8aeb-2d905c26c54f;
					- m_name = { CGIText 
						- m_str = "Requisito PWM";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.178967 0 0 0.121795 30 455.634 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=36%,64%>
<frame name=IDTextCompartment>
<frame name=SpecificationTextCompartment>";
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 1;
				}
				{ CGIAnnotation 
					- _id = GUID e044cd3f-2700-4f17-bcbd-c2445107406c;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Requirement";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "ID,Specification";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 176;
					- m_pModelObject = { IHandle 
						- _m2Class = "IRequirement";
						- _filename = "_Requisitos.sbs";
						- _subsystem = "_Requisitos";
						- _class = "";
						- _name = "Requisito ADC";
						- _id = GUID f230e846-fc6a-4648-bf73-e3e8f72330e2;
					}
					- m_pParent = GUID 21c3de7b-5b1e-4ece-8aeb-2d905c26c54f;
					- m_name = { CGIText 
						- m_str = "Requisito ADC";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.178967 0 0 0.148352 232 455.555 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=27%,73%>
<frame name=IDTextCompartment>
<frame name=SpecificationTextCompartment>";
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 1;
				}
				{ CGIAnnotation 
					- _id = GUID ae2f893e-e684-480f-9b03-d07de6491bf2;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Requirement";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "ID,Specification";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 176;
					- m_pModelObject = { IHandle 
						- _m2Class = "IRequirement";
						- _filename = "_Requisitos.sbs";
						- _subsystem = "_Requisitos";
						- _class = "";
						- _name = "Requisito CONTROLE";
						- _id = GUID cdd89261-7335-4387-a028-44076154e2b1;
					}
					- m_pParent = GUID 21c3de7b-5b1e-4ece-8aeb-2d905c26c54f;
					- m_name = { CGIText 
						- m_str = "Requisito CONTROLE";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.178967 0 0 0.148352 437 455.555 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=37%,63%>
<frame name=IDTextCompartment>
<frame name=SpecificationTextCompartment>";
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 1;
				}
				{ CGIAnnotation 
					- _id = GUID 44d1d204-0b1f-4fbe-811c-45efc8bed9b6;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Requirement";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "ID,Specification";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 176;
					- m_pModelObject = { IHandle 
						- _m2Class = "IRequirement";
						- _filename = "_Requisitos.sbs";
						- _subsystem = "_Requisitos";
						- _class = "";
						- _name = "Requisito LCD";
						- _id = GUID 14f38fe2-4ee6-4a1e-950b-e3f37eef0a0a;
					}
					- m_pParent = GUID 21c3de7b-5b1e-4ece-8aeb-2d905c26c54f;
					- m_name = { CGIText 
						- m_str = "Requisito LCD";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.178967 0 0 0.119963 232 274.64 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=30%,70%>
<frame name=IDTextCompartment>
<frame name=SpecificationTextCompartment>";
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 1;
				}
				{ CGIAnnotation 
					- _id = GUID d663e66e-1a42-4ce1-ae6d-936a23238e61;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Requirement";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "ID,Specification";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 176;
					- m_pModelObject = { IHandle 
						- _m2Class = "IRequirement";
						- _filename = "_Requisitos.sbs";
						- _subsystem = "_Requisitos";
						- _class = "";
						- _name = "Requisito DISPLAY7SEG";
						- _id = GUID a4b54609-cfab-4ccc-9983-191f2968bcf3;
					}
					- m_pParent = GUID 21c3de7b-5b1e-4ece-8aeb-2d905c26c54f;
					- m_name = { CGIText 
						- m_str = "Requisito DISPLAY7SEG";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.178967 0 0 0.113553 437 138.659 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=35%,65%>
<frame name=IDTextCompartment>
<frame name=SpecificationTextCompartment>";
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 1;
				}
				
				- m_access = 'Z';
				- m_modified = 'N';
				- m_fileVersion = "";
				- m_nModifyDate = 0;
				- m_nCreateDate = 0;
				- m_creator = "";
				- m_bScaleWithZoom = 1;
				- m_arrowStyle = 'S';
				- m_pRoot = GUID 21c3de7b-5b1e-4ece-8aeb-2d905c26c54f;
				- m_currentLeftTop = 0 0 ;
				- m_currentRightBottom = 0 0 ;
			}
			- _defaultSubsystem = { IHandle 
				- _m2Class = "ISubsystem";
				- _filename = "_Projeto_Pratico.sbs";
				- _subsystem = "";
				- _class = "";
				- _name = "_Projeto_Pratico";
				- _id = GUID 20246198-4c47-4bfe-9397-a7aa14ffd20f;
			}
		}
		{ IDiagram 
			- _id = GUID 604328de-2202-48b3-9d1a-353bbeb75331;
			- _myState = 8192;
			- _properties = { IPropertyContainer 
				- Subjects = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ IPropertySubject 
						- _Name = "Format";
						- Metaclasses = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "Comment";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,84,96";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,207";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "225,225,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Package";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,216,151";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "221,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
						}
					}
				}
			}
			- _name = "diag_pacotes";
			- _objectCreation = "515171334201693092045";
			- _umlDependencyID = "2685";
			- _lastModifiedTime = "4.11.2016::0:13:46";
			- _graphicChart = { CGIClassChart 
				- _id = GUID 84c7ed09-6a53-4e4a-925b-6e70d2f9ea4a;
				- m_type = 0;
				- m_pModelObject = { IHandle 
					- _m2Class = "IDiagram";
					- _id = GUID 604328de-2202-48b3-9d1a-353bbeb75331;
				}
				- m_pParent = ;
				- m_name = { CGIText 
					- m_str = "";
					- m_style = "Arial" 10 0 0 0 1 ;
					- m_color = { IColor 
						- m_fgColor = 0;
						- m_bgColor = 0;
						- m_bgFlag = 0;
					}
					- m_position = 1 0 0  ;
					- m_nIdent = 0;
					- m_bImplicitSetRectPoints = 0;
					- m_nOrientationCtrlPt = 8;
				}
				- m_drawBehavior = 0;
				- m_bIsPreferencesInitialized = 0;
				- elementList = 11;
				{ CGIClass 
					- _id = GUID 8b281bd3-f1f5-4938-b9c6-5a6107121e5f;
					- m_type = 78;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "_Projeto_Pratico.sbs";
						- _subsystem = "_Projeto_Pratico";
						- _class = "";
						- _name = "TopLevel";
						- _id = GUID 0d5184b0-4db2-4cdb-a85e-27b5b9b2898f;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "TopLevel";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 0;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 0 ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIAnnotation 
					- _id = GUID 58f20f87-53df-4801-9589-c23f9c68ea4e;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 173;
					- m_pModelObject = { IHandle 
						- _m2Class = "IComment";
						- _filename = "_Projeto_Pratico.sbs";
						- _subsystem = "_Projeto_Pratico";
						- _class = "";
						- _name = "comment_21";
						- _id = GUID ff49df2e-66b1-405c-9a1d-efad749c7d2c;
					}
					- m_pParent = GUID 8b281bd3-f1f5-4938-b9c6-5a6107121e5f;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.48524 0 0 0.100733 25 25.6978 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 0;
				}
				{ CGIPackage 
					- _id = GUID 8170eadf-d7c3-4067-af4b-adc22e878882;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 127;
					- m_pModelObject = { IHandle 
						- _m2Class = "ISubsystem";
						- _filename = "_Projeto_Pratico.sbs";
						- _subsystem = "";
						- _class = "";
						- _name = "_Projeto_Pratico";
						- _id = GUID 20246198-4c47-4bfe-9397-a7aa14ffd20f;
					}
					- m_pParent = GUID 8b281bd3-f1f5-4938-b9c6-5a6107121e5f;
					- m_name = { CGIText 
						- m_str = "_Projeto_Pratico";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.143914 0 0 0.0894874 25 156.311 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 0  0 1151  1216 1151  1216 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIPackage 
					- _id = GUID ae6ed687-c19d-4d04-a6f4-88d5055596d0;
					- m_type = 127;
					- m_pModelObject = { IHandle 
						- _m2Class = "ISubsystem";
						- _filename = "_Requisitos.sbs";
						- _subsystem = "";
						- _class = "";
						- _name = "_Requisitos";
						- _id = GUID 83b232d5-cbf5-48de-bd01-d866eaf248e9;
					}
					- m_pParent = GUID 8b281bd3-f1f5-4938-b9c6-5a6107121e5f;
					- m_name = { CGIText 
						- m_str = "_Requisitos";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.177632 0 0 0.0894874 289 153 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 0  0 1151  1216 1151  1216 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIPackage 
					- _id = GUID 20bc8cff-c8cd-4f3a-8345-3f4fc40920bc;
					- m_type = 127;
					- m_pModelObject = { IHandle 
						- _m2Class = "ISubsystem";
						- _filename = "LedSwi.sbs";
						- _subsystem = "";
						- _class = "";
						- _name = "LedSwi";
						- _id = GUID 065e8ea8-3104-4865-9f03-c833c5c57170;
					}
					- m_pParent = GUID 8b281bd3-f1f5-4938-b9c6-5a6107121e5f;
					- m_name = { CGIText 
						- m_str = "LedSwi";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.177632 0 0 0.0894874 287 397 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 0  0 1151  1216 1151  1216 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIPackage 
					- _id = GUID da40b410-5e50-466d-9af2-5f16d8833e86;
					- m_type = 127;
					- m_pModelObject = { IHandle 
						- _m2Class = "ISubsystem";
						- _filename = "Main.sbs";
						- _subsystem = "";
						- _class = "";
						- _name = "Main";
						- _id = GUID a9bfd00a-eefd-40b0-8807-d7abb8ac9870;
					}
					- m_pParent = GUID 8b281bd3-f1f5-4938-b9c6-5a6107121e5f;
					- m_name = { CGIText 
						- m_str = "Main";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.177632 0 0 0.0894874 25 270 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 0  0 1151  1216 1151  1216 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIPackage 
					- _id = GUID 4cc8446f-cc4d-4a69-828a-d33305f15445;
					- m_type = 127;
					- m_pModelObject = { IHandle 
						- _m2Class = "ISubsystem";
						- _filename = "KL25Z.sbs";
						- _subsystem = "";
						- _class = "";
						- _name = "KL25Z";
						- _id = GUID 9ac6e8be-1171-4050-a109-3666f2506e5d;
					}
					- m_pParent = GUID 8b281bd3-f1f5-4938-b9c6-5a6107121e5f;
					- m_name = { CGIText 
						- m_str = "KL25Z";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.177632 0 0 0.0894874 289 266 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 0  0 1151  1216 1151  1216 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIPackage 
					- _id = GUID 352f5a78-a251-4f49-9b5b-78211b51de38;
					- m_type = 127;
					- m_pModelObject = { IHandle 
						- _m2Class = "ISubsystem";
						- _filename = "Util.sbs";
						- _subsystem = "";
						- _class = "";
						- _name = "Util";
						- _id = GUID f5d6f4c4-ca70-4386-9866-389eed46d9b7;
					}
					- m_pParent = GUID 8b281bd3-f1f5-4938-b9c6-5a6107121e5f;
					- m_name = { CGIText 
						- m_str = "Util";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.177632 0 0 0.0894874 25 395 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 0  0 1151  1216 1151  1216 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIPackage 
					- _id = GUID f244c5dd-1aca-4a05-8555-c621d6b542c7;
					- m_type = 127;
					- m_pModelObject = { IHandle 
						- _m2Class = "ISubsystem";
						- _filename = "GPIO.sbs";
						- _subsystem = "";
						- _class = "";
						- _name = "GPIO";
						- _id = GUID cecafbf0-ffbd-4124-8cae-f06a2917ce91;
					}
					- m_pParent = GUID 8b281bd3-f1f5-4938-b9c6-5a6107121e5f;
					- m_name = { CGIText 
						- m_str = "GPIO";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.177632 0 0 0.13119 27 517 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 0  0 1151  1216 1151  1216 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIPackage 
					- _id = GUID 63f75952-de4d-4dad-be10-213b693fce1c;
					- m_type = 127;
					- m_pModelObject = { IHandle 
						- _m2Class = "ISubsystem";
						- _filename = "PIT.sbs";
						- _subsystem = "";
						- _class = "";
						- _name = "PIT";
						- _id = GUID 83818f05-7053-49e7-ae2f-96b665be83da;
					}
					- m_pParent = GUID 8b281bd3-f1f5-4938-b9c6-5a6107121e5f;
					- m_name = { CGIText 
						- m_str = "PIT";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.177632 0 0 0.13119 290 516 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 0  0 1151  1216 1151  1216 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIPackage 
					- _id = GUID 7436448e-c983-4a56-a9a4-42ede8ca1331;
					- m_type = 127;
					- m_pModelObject = { IHandle 
						- _m2Class = "ISubsystem";
						- _filename = "SevenSeg.sbs";
						- _subsystem = "";
						- _class = "";
						- _name = "SevenSeg";
						- _id = GUID e536725c-fa59-4de6-a2b0-d993b44d2f45;
					}
					- m_pParent = GUID 8b281bd3-f1f5-4938-b9c6-5a6107121e5f;
					- m_name = { CGIText 
						- m_str = "SevenSeg";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.177632 0 0 0.13119 29 683 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 0  0 1151  1216 1151  1216 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				
				- m_access = 'Z';
				- m_modified = 'N';
				- m_fileVersion = "";
				- m_nModifyDate = 0;
				- m_nCreateDate = 0;
				- m_creator = "";
				- m_bScaleWithZoom = 1;
				- m_arrowStyle = 'S';
				- m_pRoot = GUID 8b281bd3-f1f5-4938-b9c6-5a6107121e5f;
				- m_currentLeftTop = 0 0 ;
				- m_currentRightBottom = 0 0 ;
			}
			- _defaultSubsystem = { IHandle 
				- _m2Class = "ISubsystem";
				- _filename = "_Projeto_Pratico.sbs";
				- _subsystem = "";
				- _class = "";
				- _name = "_Projeto_Pratico";
				- _id = GUID 20246198-4c47-4bfe-9397-a7aa14ffd20f;
			}
		}
		{ IDiagram 
			- _id = GUID f53d507c-79b1-4f7f-850a-0c96a124e9bd;
			- _myState = 8192;
			- _properties = { IPropertyContainer 
				- Subjects = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ IPropertySubject 
						- _Name = "Format";
						- Metaclasses = { IRPYRawContainer 
							- size = 4;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "Association";
								- Properties = { IRPYRawContainer 
									- size = 5;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "221,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Class";
								- Properties = { IRPYRawContainer 
									- size = 8;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,34,84,148";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "121,122,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineStyle";
										- _Value = "0";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Comment";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,84,96";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,207";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "225,225,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Depends";
								- Properties = { IRPYRawContainer 
									- size = 6;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,16,230";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineStyle";
										- _Value = "1";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "0";
										- _Type = Int;
									}
								}
							}
						}
					}
				}
			}
			- _name = "diag_definicao_semana_04_05";
			- _objectCreation = "515191334201693091845";
			- _umlDependencyID = "3988";
			- _lastModifiedTime = "4.13.2016::12:33:54";
			- _graphicChart = { CGIClassChart 
				- _id = GUID 338e6526-0699-499c-b6b4-93ea64c72097;
				- m_type = 0;
				- m_pModelObject = { IHandle 
					- _m2Class = "IDiagram";
					- _id = GUID f53d507c-79b1-4f7f-850a-0c96a124e9bd;
				}
				- m_pParent = ;
				- m_name = { CGIText 
					- m_str = "";
					- m_style = "Arial" 10 0 0 0 1 ;
					- m_color = { IColor 
						- m_fgColor = 0;
						- m_bgColor = 0;
						- m_bgFlag = 0;
					}
					- m_position = 1 0 0  ;
					- m_nIdent = 0;
					- m_bImplicitSetRectPoints = 0;
					- m_nOrientationCtrlPt = 8;
				}
				- m_drawBehavior = 0;
				- m_bIsPreferencesInitialized = 0;
				- elementList = 28;
				{ CGIClass 
					- _id = GUID cbe743a9-93d8-4b8d-93fe-5a38658f4c13;
					- m_type = 78;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "_Projeto_Pratico.sbs";
						- _subsystem = "_Projeto_Pratico";
						- _class = "";
						- _name = "TopLevel";
						- _id = GUID 0d5184b0-4db2-4cdb-a85e-27b5b9b2898f;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "TopLevel";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 0;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 0 ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIAnnotation 
					- _id = GUID 6654c7a7-4f32-4645-a17d-e5044dc8b43a;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 173;
					- m_pModelObject = { IHandle 
						- _m2Class = "IComment";
						- _filename = "_Projeto_Pratico.sbs";
						- _subsystem = "_Projeto_Pratico";
						- _class = "";
						- _name = "comment_14";
						- _id = GUID dec1f94f-1152-46e1-904d-55660096766c;
					}
					- m_pParent = GUID cbe743a9-93d8-4b8d-93fe-5a38658f4c13;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.526753 0 0 0.100733 27 26.6978 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 0;
				}
				{ CGIClass 
					- _id = GUID 74124fb5-979b-4e9a-8b0e-3c0cafd61e28;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Class";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "Attribute,PrimitiveOperation,";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Main.sbs";
						- _subsystem = "Main";
						- _class = "";
						- _name = "es670";
						- _id = GUID 24edaf1f-6db0-4e29-bf9d-2cfd75f2e63c;
					}
					- m_pParent = GUID cbe743a9-93d8-4b8d-93fe-5a38658f4c13;
					- m_name = { CGIText 
						- m_str = "Main::es670";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2152;
					- m_transform = 0.151086 0 0 0.113191 217.698 124.76 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=25%,75%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Main.sbs";
							- _subsystem = "Main";
							- _class = "es670";
							- _name = "boardInit()";
							- _id = GUID 96ad7817-8150-4f17-ac8c-173f02ad5176;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Main.sbs";
							- _subsystem = "Main";
							- _class = "es670";
							- _name = "main()";
							- _id = GUID 26278d1f-734c-4aa3-8518-81c21ec1ac06;
						}
					}
				}
				{ CGIClass 
					- _id = GUID b5219761-b50a-447e-be69-1a795deec843;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Class";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Font.Size";
												- _Value = "10";
												- _Type = Int;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "LedSwi.sbs";
						- _subsystem = "LedSwi";
						- _class = "";
						- _name = "ledswi_hal";
						- _id = GUID c0445b4c-197d-4e5f-b22f-c3918af768b2;
					}
					- m_pParent = GUID cbe743a9-93d8-4b8d-93fe-5a38658f4c13;
					- m_name = { CGIText 
						- m_str = "LedSwi::ledswi_hal";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2152;
					- m_transform = 0.393768 0 0 0.152406 452.212 487.858 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=29%,71%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 1;
						- value = 
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "LedSwi.sbs";
							- _subsystem = "LedSwi";
							- _class = "ledswi_hal";
							- _name = "MAX_LED_SWI";
							- _id = GUID 1afbce5c-41cd-47e7-bb33-c2951cd736d0;
						}
					}
					- Operations = { IRPYRawContainer 
						- size = 4;
						- value = 
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "LedSwi.sbs";
							- _subsystem = "LedSwi";
							- _class = "ledswi_hal";
							- _name = "initLedSwitch(char,char)";
							- _id = GUID 4099a6e6-63e0-4f1d-8684-a0c1721afc00;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "LedSwi.sbs";
							- _subsystem = "LedSwi";
							- _class = "ledswi_hal";
							- _name = "setLed(char)";
							- _id = GUID e5bc592b-4ecc-49e1-b438-0b774c7c9304;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "LedSwi.sbs";
							- _subsystem = "LedSwi";
							- _class = "ledswi_hal";
							- _name = "clearLed(char)";
							- _id = GUID 5acfbab4-706e-474d-8889-4c6f3302ffcc;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "LedSwi.sbs";
							- _subsystem = "LedSwi";
							- _class = "ledswi_hal";
							- _name = "getSwitchStatus(char)";
							- _id = GUID a32c770b-17a9-4e1e-a689-3b534e3aa42b;
						}
					}
				}
				{ CGIClass 
					- _id = GUID 927a6cf9-d299-4188-b182-f1e287f87cad;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Util.sbs";
						- _subsystem = "Util";
						- _class = "";
						- _name = "util";
						- _id = GUID d00d39bc-27dd-42e5-87aa-b5bf491dbe5b;
					}
					- m_pParent = GUID cbe743a9-93d8-4b8d-93fe-5a38658f4c13;
					- m_name = { CGIText 
						- m_str = "Util::util";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2152;
					- m_transform = 0.175637 0 0 0.131907 153.649 435.603 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=25%,75%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 4;
						- value = 
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Util.sbs";
							- _subsystem = "Util";
							- _class = "util";
							- _name = "genDelay088us()";
							- _id = GUID 153be061-afed-4fea-b6d5-d9b9065886f1;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Util.sbs";
							- _subsystem = "Util";
							- _class = "util";
							- _name = "genDelay250us()";
							- _id = GUID 350ff3d5-d41e-4ccb-beb1-6e64d3334969;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Util.sbs";
							- _subsystem = "Util";
							- _class = "util";
							- _name = "genDelay1ms()";
							- _id = GUID ae534ce2-2a74-4e8b-be3f-07658458cc99;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Util.sbs";
							- _subsystem = "Util";
							- _class = "util";
							- _name = "genDelay10ms()";
							- _id = GUID 9ac8cefe-7f1e-4aa1-b492-663c702058a4;
						}
					}
				}
				{ CGIClass 
					- _id = GUID d8d4093c-0bb5-41ee-97df-c899c9489144;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "KL25Z.sbs";
						- _subsystem = "KL25Z";
						- _class = "";
						- _name = "es670_peripheral_board";
						- _id = GUID aa110bb3-0172-4266-a0b1-29e5f9f27d13;
					}
					- m_pParent = GUID cbe743a9-93d8-4b8d-93fe-5a38658f4c13;
					- m_name = { CGIText 
						- m_str = "KL25Z::es670_peripheral_board";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.190173 0 0 0.0882353 622.62 269.971 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIAssociationEnd 
					- _id = GUID 8a54a78b-c6f6-415c-abb0-4fa190f4cd25;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 92;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Main.sbs";
						- _subsystem = "Main";
						- _class = "es670";
						- _name = "itsLedswi_hal";
						- _id = GUID 18e5ea98-cbd6-408b-930f-9dd09b471885;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 74124fb5-979b-4e9a-8b0e-3c0cafd61e28;
					- m_sourceType = 'F';
					- m_pTarget = GUID b5219761-b50a-447e-be69-1a795deec843;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_arrow = 2 290 370  592 370  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 479 1345 ;
					- m_TargetPort = 355 375 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "";
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 1;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 1;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 1;
					- m_bShowQualifier2 = 1;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 0;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
						- m_nVerticalSpacing = -7;
						- m_nOrientationCtrlPt = 6;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = type_122;
				}
				{ CGIAssociationEnd 
					- _id = GUID 29102aa1-3178-46b4-9984-92dc4ce709e6;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 92;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Main.sbs";
						- _subsystem = "Main";
						- _class = "es670";
						- _name = "itsUtil";
						- _id = GUID 5dd7132f-b38d-474a-8785-c3020d8f6492;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 74124fb5-979b-4e9a-8b0e-3c0cafd61e28;
					- m_sourceType = 'F';
					- m_pTarget = GUID 927a6cf9-d299-4188-b182-f1e287f87cad;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 313 1380 ;
					- m_TargetPort = 634 359 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "";
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 1;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 1;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 1;
					- m_bShowQualifier2 = 1;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 0;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
						- m_nVerticalSpacing = -7;
						- m_nOrientationCtrlPt = 6;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = type_122;
				}
				{ CGIInheritance 
					- _id = GUID 6ddc7da5-db92-4e10-a91a-c359b8488ed0;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "LedSwi.sbs";
						- _subsystem = "LedSwi";
						- _class = "ledswi_hal";
						- _name = "es670_peripheral_board";
						- _id = GUID 81db235c-dc5c-49ca-a5de-e6efb160d63c;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "mclab2";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID b5219761-b50a-447e-be69-1a795deec843;
					- m_sourceType = 'F';
					- m_pTarget = GUID d8d4093c-0bb5-41ee-97df-c899c9489144;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Usage";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  57 -9  57 7  -6 7  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 1;
						- m_transform = 1 0 0 1.4375 796 520.938 ;
						- m_nHorizontalSpacing = 45;
						- m_nVerticalSpacing = 45;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 860 322 ;
					- m_TargetPort = 885 964 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIClass 
					- _id = GUID bc238bad-ba12-4b6b-9622-2b1ab455cfe0;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "_Projeto_Pratico.sbs";
						- _subsystem = "_Projeto_Pratico";
						- _class = "";
						- _name = "MKL25Z4";
						- _id = GUID d32248dd-74d9-479b-b8a9-cc8ac7ccc303;
					}
					- m_pParent = GUID cbe743a9-93d8-4b8d-93fe-5a38658f4c13;
					- m_name = { CGIText 
						- m_str = "MKL25Z4";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.0715091 0 0 0.0882353 688.129 108.971 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIInheritance 
					- _id = GUID 7357ad6b-2da6-4bd3-a9b3-5fb00e48594a;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "KL25Z.sbs";
						- _subsystem = "KL25Z";
						- _class = "es670_peripheral_board";
						- _name = "MKL25Z4";
						- _id = GUID 65e97bfc-98fc-4097-a796-5aecc62912e4;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "p18F4550";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID d8d4093c-0bb5-41ee-97df-c899c9489144;
					- m_sourceType = 'F';
					- m_pTarget = GUID bc238bad-ba12-4b6b-9622-2b1ab455cfe0;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Usage";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  62 -9  62 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 727 268 ;
						- m_nHorizontalSpacing = 49;
						- m_nVerticalSpacing = -3;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 519 340 ;
					- m_TargetPort = 468 1122 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 46f37139-7647-4282-a347-5452462e51d8;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "Main.sbs";
						- _subsystem = "Main";
						- _class = "es670";
						- _name = "es670_peripheral_board";
						- _id = GUID a76f61da-437f-4210-8cfb-c8390c8878ca;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "mclab2";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 74124fb5-979b-4e9a-8b0e-3c0cafd61e28;
					- m_sourceType = 'F';
					- m_pTarget = GUID d8d4093c-0bb5-41ee-97df-c899c9489144;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Usage";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  62 -9  62 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 412 247 ;
						- m_nHorizontalSpacing = -45;
						- m_nVerticalSpacing = -27;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 500 259  500 318  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 1001 1189 ;
					- m_TargetPort = 197 544 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 1760ad43-bf28-4c1b-a0cd-aee244b31c3b;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "Util.sbs";
						- _subsystem = "Util";
						- _class = "util";
						- _name = "es670_peripheral_board";
						- _id = GUID 947a2acf-c076-44d9-a62d-540dd1cd9c5b;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "mclab2";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 927a6cf9-d299-4188-b182-f1e287f87cad;
					- m_sourceType = 'F';
					- m_pTarget = GUID d8d4093c-0bb5-41ee-97df-c899c9489144;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Usage";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  62 -9  62 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 384 482 ;
						- m_nHorizontalSpacing = -54;
						- m_nVerticalSpacing = 23;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 481 497  481 382  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 896 465 ;
					- m_TargetPort = 333 1270 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIClass 
					- _id = GUID 3f8810d3-53ea-41d0-bdf4-0fe0a2ef434e;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Buzzer.sbs";
						- _subsystem = "Buzzer";
						- _class = "";
						- _name = "buzzer_hal";
						- _id = GUID 8c076f32-e54b-4c9f-8e0b-f6dc70637b69;
					}
					- m_pParent = GUID cbe743a9-93d8-4b8d-93fe-5a38658f4c13;
					- m_name = { CGIText 
						- m_str = "Buzzer::buzzer_hal";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2152;
					- m_transform = 0.247403 0 0 0.171122 29.5051 586.701 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=37%,63%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 5;
						- value = 
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Buzzer.sbs";
							- _subsystem = "Buzzer";
							- _class = "buzzer_hal";
							- _name = "init()";
							- _id = GUID aef584b1-280b-49ae-942a-a6bc2e23f2b9;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Buzzer.sbs";
							- _subsystem = "Buzzer";
							- _class = "buzzer_hal";
							- _name = "clearBuzz()";
							- _id = GUID 29c84150-5974-43cd-8652-6d876557e4d3;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Buzzer.sbs";
							- _subsystem = "Buzzer";
							- _class = "buzzer_hal";
							- _name = "setBuzz()";
							- _id = GUID 6561f7ec-2910-46e4-b4be-e4773d9baf35;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Buzzer.sbs";
							- _subsystem = "Buzzer";
							- _class = "buzzer_hal";
							- _name = "initPeriodic(unsigned int)";
							- _id = GUID e1e4348c-2712-4236-a92e-9fd0f6a474be;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Buzzer.sbs";
							- _subsystem = "Buzzer";
							- _class = "buzzer_hal";
							- _name = "stopPeriodic()";
							- _id = GUID 1c864e4e-fb62-43d8-bbed-a4290b99f58d;
						}
					}
				}
				{ CGIInheritance 
					- _id = GUID cd53e453-be4c-401a-84ef-31f3be353415;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "Buzzer.sbs";
						- _subsystem = "Buzzer";
						- _class = "buzzer_hal";
						- _name = "es670_peripheral_board";
						- _id = GUID 41e36bfe-b7d9-41db-9b6e-9bc30cb8ff4b;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "mclab2";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 3f8810d3-53ea-41d0-bdf4-0fe0a2ef434e;
					- m_sourceType = 'F';
					- m_pTarget = GUID d8d4093c-0bb5-41ee-97df-c899c9489144;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Usage";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  62 -9  62 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 122 337 ;
						- m_nHorizontalSpacing = -23;
						- m_nVerticalSpacing = -28;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 1 112 350  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 333 382 ;
					- m_TargetPort = 18 907 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIAnnotation 
					- _id = GUID b119d3bd-d462-4ae5-bbe8-95f9b3c178f1;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 173;
					- m_pModelObject = { IHandle 
						- _m2Class = "IComment";
						- _filename = "_Projeto_Pratico.sbs";
						- _subsystem = "_Projeto_Pratico";
						- _class = "";
						- _name = "comment_30";
						- _id = GUID 1c6aff64-4936-4d1f-a7e1-13ea01f4e0ae;
					}
					- m_pParent = GUID cbe743a9-93d8-4b8d-93fe-5a38658f4c13;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.142066 0 0 0.0457875 618 51.8626 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 0;
				}
				{ CGIAssociationEnd 
					- _id = GUID fe01c562-c5c0-4bb2-a1e9-2a39a089e9b7;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 92;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Main.sbs";
						- _subsystem = "Main";
						- _class = "es670";
						- _name = "itsBuzzer_hal";
						- _id = GUID 67033756-a20d-4713-92ed-8430dc464020;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 74124fb5-979b-4e9a-8b0e-3c0cafd61e28;
					- m_sourceType = 'F';
					- m_pTarget = GUID 3f8810d3-53ea-41d0-bdf4-0fe0a2ef434e;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_arrow = 1 66 222  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 75 859 ;
					- m_TargetPort = 148 504 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "";
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 1;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 1;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 1;
					- m_bShowQualifier2 = 1;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 4;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
						- m_nVerticalSpacing = -7;
						- m_nOrientationCtrlPt = 6;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = type_122;
				}
				{ CGIClass 
					- _id = GUID fc7bf8a3-8e00-411a-b413-44b02c835d16;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "GPIO.sbs";
						- _subsystem = "GPIO";
						- _class = "";
						- _name = "gpio_hal";
						- _id = GUID c57aad23-b8cb-48a0-8c8b-df32fa77d0e8;
					}
					- m_pParent = GUID cbe743a9-93d8-4b8d-93fe-5a38658f4c13;
					- m_name = { CGIText 
						- m_str = "GPIO::gpio_hal";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2568;
					- m_transform = 0.456091 0 0 0.208556 931.088 475.385 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 5;
						- value = 
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "GPIO.sbs";
							- _subsystem = "GPIO";
							- _class = "gpio_hal";
							- _name = "UNGATE_PORT(Port_id)";
							- _id = GUID de9d0e08-f7a8-45b4-872d-a69396d013f0;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "GPIO.sbs";
							- _subsystem = "GPIO";
							- _class = "gpio_hal";
							- _name = "INIT_PIN(Port_id,unsigned short)";
							- _id = GUID 5b4fd962-c8e6-401d-b109-2340c94cbbd8;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "GPIO.sbs";
							- _subsystem = "GPIO";
							- _class = "gpio_hal";
							- _name = "WRITE_PIN(Port_id,unsigned short,GPIO_VAL)";
							- _id = GUID d451de83-f1f4-4fbc-ad37-2cd41e62d9fb;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "GPIO.sbs";
							- _subsystem = "GPIO";
							- _class = "gpio_hal";
							- _name = "WRITE_MASK(Port_id,unsigned int,GPIO_VAL)";
							- _id = GUID c32eaa68-a82a-4204-89e1-7d955fb27299;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "GPIO.sbs";
							- _subsystem = "GPIO";
							- _class = "gpio_hal";
							- _name = "READ_PIN(Port_id,unsigned short)";
							- _id = GUID 9a3098fb-33a3-4301-813e-e2bf70187cbd;
						}
					}
				}
				{ CGIInheritance 
					- _id = GUID cd75ee9d-0613-46cf-b6c5-f2bb3f73bb1f;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "GPIO.sbs";
						- _subsystem = "GPIO";
						- _class = "gpio_hal";
						- _name = "es670_peripheral_board";
						- _id = GUID 89bf952f-047e-4e41-b827-59bd040242fc;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "es670_peripheral_board";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID fc7bf8a3-8e00-411a-b413-44b02c835d16;
					- m_sourceType = 'F';
					- m_pTarget = GUID d8d4093c-0bb5-41ee-97df-c899c9489144;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Usage";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  57 -9  57 7  -6 7  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 1;
						- m_transform = 1 0 0 0.8125 1009 526.312 ;
						- m_nHorizontalSpacing = 26;
						- m_nVerticalSpacing = 146;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 1 994 347  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 136 348 ;
					- m_TargetPort = 980 873 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID f217db14-a986-4566-9639-727aa0dc26b9;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "Buzzer.sbs";
						- _subsystem = "Buzzer";
						- _class = "buzzer_hal";
						- _name = "gpio_hal";
						- _id = GUID 4431a3ed-6d6c-4df5-858d-d66056a37455;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "gpio_hal";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 3f8810d3-53ea-41d0-bdf4-0fe0a2ef434e;
					- m_sourceType = 'F';
					- m_pTarget = GUID fc7bf8a3-8e00-411a-b413-44b02c835d16;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Usage";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  57 -9  57 7  -6 7  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 297 720 ;
						- m_nHorizontalSpacing = -258;
						- m_nVerticalSpacing = -36;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 1004 878 ;
					- m_TargetPort = 25 1269 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIClass 
					- _id = GUID d4dcef82-cab7-4d4c-ab4d-7748879a35a3;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "PIT.sbs";
						- _subsystem = "PIT";
						- _class = "";
						- _name = "pit_hal";
						- _id = GUID fa912741-cd5a-4430-b673-07d24c4ba7be;
					}
					- m_pParent = GUID cbe743a9-93d8-4b8d-93fe-5a38658f4c13;
					- m_name = { CGIText 
						- m_str = "PIT::pit_hal";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2568;
					- m_transform = 0.602455 0 0 0.198752 933.795 818.61 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 5;
						- value = 
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "PIT.sbs";
							- _subsystem = "PIT";
							- _class = "pit_hal";
							- _name = "enable(unsigned short)";
							- _id = GUID 29fa486c-d9cc-49e1-8cd6-fa74880c92f2;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "PIT.sbs";
							- _subsystem = "PIT";
							- _class = "pit_hal";
							- _name = "start_timer_interrupt(unsigned short,unsigned int,void *)";
							- _id = GUID 868df793-13b1-42b8-b167-68ac00cf9069;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "PIT.sbs";
							- _subsystem = "PIT";
							- _class = "pit_hal";
							- _name = "stop_timer_interrupt(unsigned int)";
							- _id = GUID 492eb741-c8f4-4901-80c6-18df278a3d46;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "PIT.sbs";
							- _subsystem = "PIT";
							- _class = "pit_hal";
							- _name = "mark_interrupt_handled(unsigned short)";
							- _id = GUID c373f3fd-3719-4b1d-903e-8f63ca680dac;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "PIT.sbs";
							- _subsystem = "PIT";
							- _class = "pit_hal";
							- _name = "PIT_IRQHandler()";
							- _id = GUID 68d4da25-dd51-4d94-9486-9db8ede0df57;
						}
					}
				}
				{ CGIInheritance 
					- _id = GUID c5c47c63-2a92-4906-b767-8e5af39c4bb8;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "PIT.sbs";
						- _subsystem = "PIT";
						- _class = "pit_hal";
						- _name = "es670_peripheral_board";
						- _id = GUID 30e57f27-5f4b-40e4-890a-20404d673b81;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "es670_peripheral_board";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID d4dcef82-cab7-4d4c-ab4d-7748879a35a3;
					- m_sourceType = 'F';
					- m_pTarget = GUID d8d4093c-0bb5-41ee-97df-c899c9489144;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Usage";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  57 -9  57 7  -6 7  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 1533 817 ;
						- m_nHorizontalSpacing = 38;
						- m_nVerticalSpacing = 485;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 1 1520 316  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 966 335 ;
					- m_TargetPort = 985 522 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIClass 
					- _id = GUID 6c2246e0-8924-4840-9d0b-952c38560024;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "SevenSeg.sbs";
						- _subsystem = "SevenSeg";
						- _class = "";
						- _name = "sevenseg_hal";
						- _id = GUID d3ae0a03-e91c-4d6a-8e91-113b264b5ef8;
					}
					- m_pParent = GUID cbe743a9-93d8-4b8d-93fe-5a38658f4c13;
					- m_name = { CGIText 
						- m_str = "SevenSeg::sevenseg_hal";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2824;
					- m_transform = 0.40982 0 0 0.226381 323.181 713.521 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "SevenSeg.sbs";
							- _subsystem = "SevenSeg";
							- _class = "sevenseg_hal";
							- _name = "MAX_SEGMENT_NUMBER";
							- _id = GUID 8e86b917-b700-4a77-bbf4-00f271a053f1;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "SevenSeg.sbs";
							- _subsystem = "SevenSeg";
							- _class = "sevenseg_hal";
							- _name = "MAX_DISP_NUMBER";
							- _id = GUID 7140231f-652a-42ed-b2c8-ce6ba52b9f3a;
						}
					}
					- Operations = { IRPYRawContainer 
						- size = 7;
						- value = 
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "SevenSeg.sbs";
							- _subsystem = "SevenSeg";
							- _class = "sevenseg_hal";
							- _name = "init()";
							- _id = GUID c93fa302-e40a-4654-97d1-e210633b2f4b;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "SevenSeg.sbs";
							- _subsystem = "SevenSeg";
							- _class = "sevenseg_hal";
							- _name = "setSegs(seven_segment_seg_type_e)";
							- _id = GUID 3d96518a-5b41-4a36-a681-ff49bde8cd96;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "SevenSeg.sbs";
							- _subsystem = "SevenSeg";
							- _class = "sevenseg_hal";
							- _name = "setDisp(seven_segment_disp_type_e)";
							- _id = GUID f83de8e2-eee8-4c6e-a07d-ce04face1b4d;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "SevenSeg.sbs";
							- _subsystem = "SevenSeg";
							- _class = "sevenseg_hal";
							- _name = "printHex(unsigned int)";
							- _id = GUID a083fe61-f281-4a43-8b5d-32f312c36e19;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "SevenSeg.sbs";
							- _subsystem = "SevenSeg";
							- _class = "sevenseg_hal";
							- _name = "printDec(unsigned int)";
							- _id = GUID 2f16c6cf-c5a2-4df9-a3f6-566c189d6f07;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "SevenSeg.sbs";
							- _subsystem = "SevenSeg";
							- _class = "sevenseg_hal";
							- _name = "dec2segArray(unsigned short,seven_segment_seg_type_e)";
							- _id = GUID f22579dd-0594-48ec-a7ee-1a12a4e4ff0e;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "SevenSeg.sbs";
							- _subsystem = "SevenSeg";
							- _class = "sevenseg_hal";
							- _name = "hex2segArray(unsigned short,seven_segment_seg_type_e)";
							- _id = GUID ef9b6900-9958-4fe9-a30d-d6d5c9459d65;
						}
					}
				}
				{ CGIInheritance 
					- _id = GUID b4d54726-0684-41f1-8993-51f507a8427f;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "SevenSeg.sbs";
						- _subsystem = "SevenSeg";
						- _class = "sevenseg_hal";
						- _name = "es670_peripheral_board_0";
						- _id = GUID f1fae246-1b3e-4b89-9cda-6b9a235b1893;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "es670_peripheral_board_0";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 6c2246e0-8924-4840-9d0b-952c38560024;
					- m_sourceType = 'F';
					- m_pTarget = GUID d8d4093c-0bb5-41ee-97df-c899c9489144;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Usage";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  57 -9  57 7  -6 7  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 1;
						- m_transform = 1 0 0 0.6875 789 793.188 ;
						- m_nHorizontalSpacing = -51;
						- m_nVerticalSpacing = 138;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 880 804  880 375  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 1044 400 ;
					- m_TargetPort = 1033 1190 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID bd5ca6d5-bbc0-49d9-b458-3d6e569ce117;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "SevenSeg.sbs";
						- _subsystem = "SevenSeg";
						- _class = "sevenseg_hal";
						- _name = "gpio_hal_0";
						- _id = GUID 279bebd8-4cb0-4d46-bc0e-b594c4c10265;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "gpio_hal_0";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 6c2246e0-8924-4840-9d0b-952c38560024;
					- m_sourceType = 'F';
					- m_pTarget = GUID fc7bf8a3-8e00-411a-b413-44b02c835d16;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Usage";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  57 -9  57 7  -6 7  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 785 835 ;
						- m_nHorizontalSpacing = -101;
						- m_nVerticalSpacing = -23;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 1 1036 842  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 1061 568 ;
					- m_TargetPort = 232 1350 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID a3b00cea-71cc-45f4-a96a-8ae357687e5d;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "SevenSeg.sbs";
						- _subsystem = "SevenSeg";
						- _class = "sevenseg_hal";
						- _name = "pit_hal";
						- _id = GUID 8508a870-3fde-4bdb-9dcb-57a7b7af6ee9;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "pit_hal";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 6c2246e0-8924-4840-9d0b-952c38560024;
					- m_sourceType = 'F';
					- m_pTarget = GUID d4dcef82-cab7-4d4c-ab4d-7748879a35a3;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Usage";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  57 -9  57 7  -6 7  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 793 926 ;
						- m_nHorizontalSpacing = -20;
						- m_nVerticalSpacing = -25;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 1039 1018 ;
					- m_TargetPort = 73 647 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIAssociationEnd 
					- _id = GUID 5581312d-b027-49af-9c58-7021a7bab820;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 92;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Main.sbs";
						- _subsystem = "Main";
						- _class = "es670";
						- _name = "itsSevenseg_hal";
						- _id = GUID 8f7ee439-31c0-46c9-92e8-1d871229631b;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 74124fb5-979b-4e9a-8b0e-3c0cafd61e28;
					- m_sourceType = 'F';
					- m_pTarget = GUID 6c2246e0-8924-4840-9d0b-952c38560024;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 942 1433 ;
					- m_TargetPort = 90 369 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "";
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 1;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 1;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 1;
					- m_bShowQualifier2 = 1;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 0;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
						- m_nVerticalSpacing = -7;
						- m_nOrientationCtrlPt = 6;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = type_122;
				}
				{ CGIInheritance 
					- _id = GUID a96cfe5a-90d1-44da-8bf5-29e40209473e;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "Buzzer.sbs";
						- _subsystem = "Buzzer";
						- _class = "buzzer_hal";
						- _name = "pit_hal";
						- _id = GUID f1188ff2-452b-44e5-be71-c3568da2f62e;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "pit_hal";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 3f8810d3-53ea-41d0-bdf4-0fe0a2ef434e;
					- m_sourceType = 'F';
					- m_pTarget = GUID d4dcef82-cab7-4d4c-ab4d-7748879a35a3;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Usage";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  57 -9  57 7  -6 7  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 175 856 ;
						- m_nHorizontalSpacing = -218;
						- m_nVerticalSpacing = -214;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 1 236 1090  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 835 1431 ;
					- m_TargetPort = 4 1389 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				
				- m_access = 'Z';
				- m_modified = 'N';
				- m_fileVersion = "";
				- m_nModifyDate = 0;
				- m_nCreateDate = 0;
				- m_creator = "";
				- m_bScaleWithZoom = 1;
				- m_arrowStyle = 'S';
				- m_pRoot = GUID cbe743a9-93d8-4b8d-93fe-5a38658f4c13;
				- m_currentLeftTop = 0 0 ;
				- m_currentRightBottom = 0 0 ;
			}
			- _defaultSubsystem = { IHandle 
				- _m2Class = "ISubsystem";
				- _filename = "_Projeto_Pratico.sbs";
				- _subsystem = "";
				- _class = "";
				- _name = "_Projeto_Pratico";
				- _id = GUID 20246198-4c47-4bfe-9397-a7aa14ffd20f;
			}
		}
	}
	- Components = { IRPYRawContainer 
		- size = 1;
		- value = 
		{ IComponent 
			- fileName = "FRDM_KL25Z";
			- _id = GUID 97403057-80a5-4323-8421-7b4a31e27ebf;
		}
	}
}

