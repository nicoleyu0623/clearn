//
// This file was generated by the JavaTM Architecture for XML Binding(JAXB) Reference Implementation, v2.2.8-b130911.1802 
// See <a href="http://java.sun.com/xml/jaxb">http://java.sun.com/xml/jaxb</a> 
// Any modifications to this file will be lost upon recompilation of the source schema. 
// Generated on: 2020.08.01 at 01:25:50 PM CEST 
//


package org.slzdevsnp.binding.tmtrading;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.bind.annotation.XmlAnyAttribute;
import javax.xml.bind.annotation.XmlAnyElement;
import javax.xml.bind.annotation.XmlAttribute;
import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlRootElement;
import javax.xml.bind.annotation.XmlType;
import javax.xml.namespace.QName;
import org.w3c.dom.Element;


/**
 * <p>Java class for anonymous complex type.
 * 
 * <p>The following schema fragment specifies the expected content contained within this class.
 * 
 * <pre>
 * &lt;complexType>
 *   &lt;complexContent>
 *     &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
 *       &lt;sequence>
 *         &lt;element name="StandardHeader" type="{http://www.deutsche-boerse.com/m7/v6}StandardHeaderType"/>
 *         &lt;element name="OrdrList">
 *           &lt;complexType>
 *             &lt;complexContent>
 *               &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
 *                 &lt;sequence>
 *                   &lt;element name="Ordr" type="{http://www.deutsche-boerse.com/m7/v6}OrdrEntryType" maxOccurs="unbounded"/>
 *                 &lt;/sequence>
 *                 &lt;anyAttribute processContents='lax'/>
 *               &lt;/restriction>
 *             &lt;/complexContent>
 *           &lt;/complexType>
 *         &lt;/element>
 *         &lt;any processContents='skip' maxOccurs="unbounded" minOccurs="0"/>
 *       &lt;/sequence>
 *       &lt;attribute name="listExecInst" type="{http://www.deutsche-boerse.com/m7/v6}ListExecInstUnionType" />
 *       &lt;anyAttribute processContents='lax'/>
 *     &lt;/restriction>
 *   &lt;/complexContent>
 * &lt;/complexType>
 * </pre>
 * 
 * 
 */
@XmlAccessorType(XmlAccessType.FIELD)
@XmlType(name = "", propOrder = {
    "standardHeader",
    "ordrList",
    "any"
})
@XmlRootElement(name = "OrdrEntry")
public class OrdrEntry {

    @XmlElement(name = "StandardHeader", required = true)
    protected StandardHeaderType standardHeader;
    @XmlElement(name = "OrdrList", required = true)
    protected OrdrEntry.OrdrList ordrList;
    @XmlAnyElement
    protected List<Element> any;
    @XmlAttribute(name = "listExecInst")
    protected String listExecInst;
    @XmlAnyAttribute
    private Map<QName, String> otherAttributes = new HashMap<QName, String>();

    /**
     * Gets the value of the standardHeader property.
     * 
     * @return
     *     possible object is
     *     {@link StandardHeaderType }
     *     
     */
    public StandardHeaderType getStandardHeader() {
        return standardHeader;
    }

    /**
     * Sets the value of the standardHeader property.
     * 
     * @param value
     *     allowed object is
     *     {@link StandardHeaderType }
     *     
     */
    public void setStandardHeader(StandardHeaderType value) {
        this.standardHeader = value;
    }

    /**
     * Gets the value of the ordrList property.
     * 
     * @return
     *     possible object is
     *     {@link OrdrEntry.OrdrList }
     *     
     */
    public OrdrEntry.OrdrList getOrdrList() {
        return ordrList;
    }

    /**
     * Sets the value of the ordrList property.
     * 
     * @param value
     *     allowed object is
     *     {@link OrdrEntry.OrdrList }
     *     
     */
    public void setOrdrList(OrdrEntry.OrdrList value) {
        this.ordrList = value;
    }

    /**
     * Gets the value of the any property.
     * 
     * <p>
     * This accessor method returns a reference to the live list,
     * not a snapshot. Therefore any modification you make to the
     * returned list will be present inside the JAXB object.
     * This is why there is not a <CODE>set</CODE> method for the any property.
     * 
     * <p>
     * For example, to add a new item, do as follows:
     * <pre>
     *    getAny().add(newItem);
     * </pre>
     * 
     * 
     * <p>
     * Objects of the following type(s) are allowed in the list
     * {@link Element }
     * 
     * 
     */
    public List<Element> getAny() {
        if (any == null) {
            any = new ArrayList<Element>();
        }
        return this.any;
    }

    /**
     * Gets the value of the listExecInst property.
     * 
     * @return
     *     possible object is
     *     {@link String }
     *     
     */
    public String getListExecInst() {
        return listExecInst;
    }

    /**
     * Sets the value of the listExecInst property.
     * 
     * @param value
     *     allowed object is
     *     {@link String }
     *     
     */
    public void setListExecInst(String value) {
        this.listExecInst = value;
    }

    /**
     * Gets a map that contains attributes that aren't bound to any typed property on this class.
     * 
     * <p>
     * the map is keyed by the name of the attribute and 
     * the value is the string value of the attribute.
     * 
     * the map returned by this method is live, and you can add new attribute
     * by updating the map directly. Because of this design, there's no setter.
     * 
     * 
     * @return
     *     always non-null
     */
    public Map<QName, String> getOtherAttributes() {
        return otherAttributes;
    }


    /**
     * <p>Java class for anonymous complex type.
     * 
     * <p>The following schema fragment specifies the expected content contained within this class.
     * 
     * <pre>
     * &lt;complexType>
     *   &lt;complexContent>
     *     &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
     *       &lt;sequence>
     *         &lt;element name="Ordr" type="{http://www.deutsche-boerse.com/m7/v6}OrdrEntryType" maxOccurs="unbounded"/>
     *       &lt;/sequence>
     *       &lt;anyAttribute processContents='lax'/>
     *     &lt;/restriction>
     *   &lt;/complexContent>
     * &lt;/complexType>
     * </pre>
     * 
     * 
     */
    @XmlAccessorType(XmlAccessType.FIELD)
    @XmlType(name = "", propOrder = {
        "ordr"
    })
    public static class OrdrList {

        @XmlElement(name = "Ordr", required = true)
        protected List<OrdrEntryType> ordr;
        @XmlAnyAttribute
        private Map<QName, String> otherAttributes = new HashMap<QName, String>();

        /**
         * Gets the value of the ordr property.
         * 
         * <p>
         * This accessor method returns a reference to the live list,
         * not a snapshot. Therefore any modification you make to the
         * returned list will be present inside the JAXB object.
         * This is why there is not a <CODE>set</CODE> method for the ordr property.
         * 
         * <p>
         * For example, to add a new item, do as follows:
         * <pre>
         *    getOrdr().add(newItem);
         * </pre>
         * 
         * 
         * <p>
         * Objects of the following type(s) are allowed in the list
         * {@link OrdrEntryType }
         * 
         * 
         */
        public List<OrdrEntryType> getOrdr() {
            if (ordr == null) {
                ordr = new ArrayList<OrdrEntryType>();
            }
            return this.ordr;
        }

        /**
         * Gets a map that contains attributes that aren't bound to any typed property on this class.
         * 
         * <p>
         * the map is keyed by the name of the attribute and 
         * the value is the string value of the attribute.
         * 
         * the map returned by this method is live, and you can add new attribute
         * by updating the map directly. Because of this design, there's no setter.
         * 
         * 
         * @return
         *     always non-null
         */
        public Map<QName, String> getOtherAttributes() {
            return otherAttributes;
        }

    }

}