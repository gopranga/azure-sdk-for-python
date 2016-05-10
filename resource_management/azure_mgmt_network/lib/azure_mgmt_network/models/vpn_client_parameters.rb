# encoding: utf-8
# Code generated by Microsoft (R) AutoRest Code Generator 0.16.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.

module Azure::ARM::Network
  module Models
    #
    # VpnClientParameters
    #
    class VpnClientParameters

      include MsRestAzure

      # @return [ProcessorArchitecture] VPN client Processor Architecture
      # -Amd64/X86. Possible values include: 'Amd64', 'X86'
      attr_accessor :processor_architecture

      #
      # Validate the object. Throws ValidationError if validation fails.
      #
      def validate
      end

      #
      # Serializes given Model object into Ruby Hash.
      # @param object Model object to serialize.
      # @return [Hash] Serialized object in form of Ruby Hash.
      #
      def self.serialize_object(object)
        object.validate
        output_object = {}

        serialized_property = object.processor_architecture
        output_object['ProcessorArchitecture'] = serialized_property unless serialized_property.nil?

        output_object
      end

      #
      # Deserializes given Ruby Hash into Model object.
      # @param object [Hash] Ruby Hash object to deserialize.
      # @return [VpnClientParameters] Deserialized object.
      #
      def self.deserialize_object(object)
        return if object.nil?
        output_object = VpnClientParameters.new

        deserialized_property = object['ProcessorArchitecture']
        if (!deserialized_property.nil? && !deserialized_property.empty?)
          enum_is_valid = ProcessorArchitecture.constants.any? { |e| ProcessorArchitecture.const_get(e).to_s.downcase == deserialized_property.downcase }
          warn 'Enum ProcessorArchitecture does not contain ' + deserialized_property.downcase + ', but was received from the server.' unless enum_is_valid
        end
        output_object.processor_architecture = deserialized_property

        output_object
      end
    end
  end
end